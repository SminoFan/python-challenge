#Brandon Coleman
#Data Analytics
#4-30-2019
#Homework 3 Python Challenge

import os
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')
output_file = os.path.join("FAnalysis.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)
    num_months = sum (1 for row in csvreader)
    min_value = 0
    min_index = 0
    max_value = 0
    max_index = 0
    dates, revenue = [],[]
 
    csvfile.seek(0)
    next(csvreader)
    
    for row in csvreader:
      revenue.append(int(row[1]))
      dates.append(row[0])  
   
    min_value = min(revenue)
    min_index = revenue.index(min(revenue)) 
    max_value = max(revenue)
    max_index = revenue.index(max(revenue))    
    average = round( (sum(revenue) / num_months), 2)
    
    
    print("\nFinancial Analysis\n--------------------------------------")
    print(f"Total Months: {num_months}")   
    print(f"Total: ${sum(revenue)}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase In Profits: {dates[max_index]} (${max_value})")
    print(f"Greatest Decrease In Profits: {dates[min_index]} (${min_value})")

    with open("output.txt", "w") as text_file:
      text_file.write("\nFinancial Analysis\n--------------------------------------\n")
      text_file.write(f"Total Months: {num_months}\n")
      text_file.write(f"Total: ${sum(revenue)}\n")
      text_file.write(f"Average Change: ${average}\n")
      text_file.write(f"Greatest Increase In Profits: {dates[max_index]} (${max_value})\n")
      text_file.write(f"Greatest Decrease In Profits: {dates[min_index]} (${min_value})\n")