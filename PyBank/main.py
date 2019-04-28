import os
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)
    num_months = sum (1 for row in csvreader)
    dates, profits = [],[]
    print(num_months)
    profits = 0
    money = 0
    csvfile.seek(0)
    next(csvreader)
    for row in csvreader:
      profits = profits + int(row[1])
      money = int(row[1])
      dates.append(row[0])   
   
    print(f"Total : {profits}")
    csvfile.seek(0)
    

