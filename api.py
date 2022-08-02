# function=CURRENCY_EXHANGE_RATE
# from_currency=USD 
# to_currency=SGD


from fileinput import close
import re,requests
import json
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=TBUDCGEFDX8LB73R'
r = requests.get(url)
data = r.json()
#dict_keys(['Realtime Currency Exchange Rate'])


for i in data.values():
    print(i)

print(json.dumps(data['Realtime Currency Exchange Rate'], indent=4))
for file in data:
    USD=re.findall(pattern="[Exchange Rate]", string=data)


