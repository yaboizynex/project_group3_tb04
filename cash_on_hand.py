# programm to calc if the cash on hand on the following day is less than the previous day
from pathlib import Path
import csv

file_path= Path.cwd()/"CashonHand.csv"

with open('Cash on Hand.csv') as csv_file:
    triggered = False  # to keep track of if any this happens even once
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    previous_cash = 0  # keep track of the cash on the previous day
    for row in csv_reader:
        if line_count == 0:   # to skip the first line of headers
          pass
        else:
            day, cash = int(row[0]), int(row[1])  # getting the day and the cash
            if ((cash - previous_cash) < 0):
                triggered = True
                print(
                    f"Cash on hand, on day {day} is lower than that on the previous day by {previous_cash - cash}")
            print(f"Difference in day {day-1} and day {day} is {cash-previous_cash} dollars")
            previous_cash = cash
        line_count += 1

if(not triggered):
  print("The cash on hand on each day was more than to previous day, no days to highlight.")
