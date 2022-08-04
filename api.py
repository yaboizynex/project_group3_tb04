 function=CURRENCY_EXHANGE_RATE
# from_currency=USD 
# to_currency=SGD


from fileinput import close
import csv
from pathlib import Path
import re,requests
import json
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=TBUDCGEFDX8LB73R'
r = requests.get(url)
data = r.json()
#dict_keys(['Realtime Currency Exchange Rate'])


for i in data.values():
    print(i)

x=json.dumps(data['Realtime Currency Exchange Rate'], indent=4)
print(x)
def CURRENCY_EXHANGE_RATE():
   fp=Path.cwd()/"summary.text"
   fp.touch()
   with fp.open(mode = "w", encoding="UTF-8", newline="")as file:

    
    
################################
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
    writer.writerow(["[HIGHEST OVERHEADS] SALARY EXPENSE: SGD39.9"])
    writer.writerow(["[CASH SURPLUS]"])
    writer.writerow(["[NET PROFIT SURPLUS]"])
    for eachIDD in exchange_rate [""]:
        writer.writerow(eachIDD["date"],eachIDD["value"])

