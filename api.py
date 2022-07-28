# 1.	Make an API call  to https://www.alphavantage.co to extract forex (FX) with the following API parameters:
function=FX_WEEKLY
from_currency=USD 
to_currency=SGD
# Find the mean of the weekly closing forex price from the after extracting the forex as JSON data.

import requests
url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=TBUDCGEFDX8LB73R'
response=requests.get(url)
USD= response.json()
print(USD)
import csv
from pathlib import Path


