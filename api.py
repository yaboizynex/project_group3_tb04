
import requests
api_key = "TBUDCGEFDX8LB73R"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response= requests.get(url)

# # print(response.json())
exchange_rate= response.json()
# import json
# #print(json.dumps(inflation, indent=4))
# for eachIDD in exchange_rate ["data"]4
# print(eachIDD['value'])
import csv
from pathlib import Path

fp_write=Path.cwd()/"summary.txt"
fp_write.touch()
with fp_write.open(mode= "w", encoding="utf-8", newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD1.38537"])
    writer.writerow(["[HIGHEST OVERHEADS] RENTAL EXPENSE: SGD33.03"])
    writer.writerow(["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"])
    writer.writerow(["[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"])
    for eachIDD in exchange_rate [""]:
        writer.writerow(eachIDD["date"],eachIDD["value"])

