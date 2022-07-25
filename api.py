import requests
api_key = "F2UE00AWKLCI7DKV"
#https://www.alphavantage.co/query?function=INFLATION&apikey=demo

url = f"https://www.alphavantage.co/query?function=INFLATION&apikey={api_key}"
response=requests.get(url)
#print(response)
#print(response.json())
inflation= response.json()
#print(inflation)

#import json
#print(json.dumps(inflation, indent=4))
#print(inflation["data"])

#for smthg in inflation["data"]:
    # print(smthg)
    #print(smthg['data'])

    #print(smthg['value'])

import csv
from pathlib import Path

fp=Path.cwd()/"inflation.csv"
fp.touch()

with fp.open(mode = "w", encoding="UTF-8", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Date","Inflation"])

    for smthg in inflation["data"]:
        writer.writerow([smthg["date"], smthg["value"]])
