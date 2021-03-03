import requests
import json

def getvalue(h):
    r = requests.get("https://blockchain.info/ru/ticker")

    d = json.loads(r.text)
    CUR = (d[h]["last"])
    RUB = (d["RUB"]["last"])
    value = RUB / CUR
    return value

a = getvalue("USD")
print(a)
