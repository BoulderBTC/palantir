import json
import requests
from multiprocessing import Pool

filepath = "addrs"

def isPool(ipaddr):
    result = None
    try:
        r = requests.get("http://{}:9327/fee".format(ipaddr), timeout=5)
        if r.ok:
            result = ipaddr
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        pass
    return result

if __name__ == "__main__":
    raw = ""
    with open(filepath, "r") as addr_file:
        raw = addr_file.read()

    addrs = [x[0][0] for x in json.loads(raw)]

    pool = Pool(processes=2000)
    result = pool.map(isPool, addrs)
    print [x for x in result if not x is None]