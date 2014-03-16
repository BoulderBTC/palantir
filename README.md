palantir
========

P2Pool node scanner in Python 


You will need mongo as well as python-eve, requests, and celery.


and then you need to run runserver.py and prime the api with a node for each coin you want to scan

  import requests
  import json
  
  headers = {"content-type": "application/json"}
  url = "http://palantir.boulderbtc.com:5005/pools/"
  
  payload = {
             "ip": "72.18.213.74",
             "coins": ["spaincoin"],
             }
  r = requests.post(url, headers=headers, data=json.dumps(payload))
  if r.ok:
      print r.json()
  else:
      print r.text
      
  print r.ok

currently only these coins will work but to get others to work is trivial:

    "litecoin": "9327",
    "bitcoin": "9332",
    "auroracoin": "12347",
    "dogecoin": "22550",
    "spaincoin": "25490",
    
    
to start celery (from the same dir as runserver.py):

    celery -A palantir.tasks wor--loglevel=info --beat
