from celery import Celery
import requests
import json
from palantir import celeryconfig

app = Celery('tasks')

ports_dict = {
    "litecoin": "9327",
    "bitcoin": "9332",
    "auroracoin": "12347",
    "dogecoin": "22550",
}

def isPool(ipaddr, port):
    result = None
    try:
        r = requests.get("http://{0}:{1}/fee".format(ipaddr, port), timeout=20)
        if r.ok:
            result = ipaddr
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        pass
    return result


app.config_from_object(celeryconfig)
api_url = "http://127.0.0.1:5005/pools/"

@app.task
def get_peers(pool):
    url = "http://{0}:{1}/peer_addresses".format(pool["ip"], ports_dict[pool["coin"]])

    r = requests.get(url, timeout=10)
    assert(r.ok)
    data = r.json().split()
    for ip in data:
        ip = ip.split(":")[0]
        if isPool(ip, ports_dict[pool["coin"]]):
            headers = {'Content-Type': 'application/json'}
            data = {"ip": ip, "coin": pool["coin"]}
            r = requests.post(api_url, headers=headers, data=json.dumps(data))



@app.task
def get_geolocation(pool):
    url = "http://freegeoip.net/json/{0}".format(pool["ip"])
    r = requests.get(url)
    assert(r.ok)
    data = r.json()

    if data["city"] and data["latitude"] and data["longitude"]:
        payload = {"location": {}}
        #human readable version
        human = data["city"]
        if data["region_name"]:
            human += ", " + data["region_name"]
        if data["country_name"]:
            human += " " + data["country_name"]

        payload["location"]["string"] = human
        payload["location"]["latitude"] = data["latitude"]
        payload["location"]["longitude"] = data["longitude"]
        headers = {'Content-Type': 'application/json', 'If-Match': pool["_etag"]}
        url = api_url + pool["_id"]
        r = requests.patch(url, headers=headers, data=json.dumps(payload))
        if r.ok:
            print r.json()



@app.task
def get_pools():
    r = requests.get(api_url)
    assert(r.ok)
    data = r.json()
    for l in data["_items"]:
        get_peers.delay(l)
        if "location" not in l:
            get_geolocation.delay(l)
