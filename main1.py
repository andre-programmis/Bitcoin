import requests
import json

def getvalue(h):
    r = requests.get('https://blockchain.info/ru/ticker')
    r_dict = json.loads(r.text)
    return r_dict[h]

f = getvalue("RUB")
print(f)
