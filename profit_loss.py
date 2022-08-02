from pathlib import Path
import csv

file_path= Path.cwd()/"Profit and Loss.csv"

days=[]#list for days
netprofit=[]#list for functions
def profit_and_loss():
     """
    - This function will highlight the day where net profit is lower than the previous day and the value
difference.
    """  
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:#readinf csv file
        # instantiate a reader object
            reader = csv.DictReader(file)
            for column in reader:
                days.append(column["Day"])#appending days into its list
                netprofit.append(column["Net Profit"])#appending netprofit into its list
map_netprofit= map(int, netprofit)#maps each string into an integer
int_netprofit=list(map_netprofit)#Converts mapped output to a list of ints
# checking if previous day's net profit is smaller in present day using a for loop
for idx in range(0, len(netprofit)):
    if int_netprofit[idx - 1] < int_netprofit[idx]:
        continue
    else:
        diff_in_netprofit=int_netprofit[idx-1]-int_netprofit[idx]
        print(f'Net Profit of Day {days[idx]} is lower than Day {days[idx-1]}. The difference is ${diff_in_netprofit}')  #fufillling brief
