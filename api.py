# 1.	Make an API call  to https://www.alphavantage.co to extract forex (FX) with the following API parameters:
function=FX_WEEKLY
from_symbol=USD 
to_symbol=SGD
# Find the mean of the weekly closing forex price from the after extracting the forex as JSON data.

import requests
url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=TBUDCGEFDX8LB73R'
response=requests.get(url)
FX_WEEKLY= response.json()
print(FX_WEEKLY)
import csv
from pathlib import Path

fp=Path.cwd()/"FX_WEEKLY.csv"
fp.touch()

with fp.open(mode = "w", encoding="UTF-8", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Date","FX_WEEKLY"])

    for smthg in FX_WEEKLY(''):
        writer.writerow([smthg["date"], smthg["value"]])
