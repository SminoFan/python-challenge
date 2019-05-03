#Brandon Coleman
#Data Analytics
#4-30-2019
#Homework 3 Python Challenge

import os
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')

output_file = os.path.join("output.txt")


#Open budget csv file 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)
    num_months = sum (1 for row in csvreader)
    min_value = 0
    min_index = 0
    max_value = 0
    max_index = 0
    dates, revenue = [],[]
 
    csvfile.seek(0) #return to beginning of csv file
    next(csvreader) #grab header again
    
    #append dates and profits to separate lists
    for row in csvreader:
      revenue.append(int(row[1]))
      dates.append(row[0])  
   
    min_value = min(revenue) #Get biggest decrease
    min_index = revenue.index(min(revenue)) #Get index of biggest increase
    max_value = max(revenue) #Get biggest increase
    max_index = revenue.index(max(revenue)) #Grab position in list of biggest increase  
    average = round( (sum(revenue) / num_months), 2) #average change over 

    #create and write to text file
    with open(output_file, "a") as text_file:
      text_file.write("Financial Analysis\n--------------------------------------\n")
      text_file.write(f"Total Months: {num_months}\n")
      text_file.write(f"Total: ${sum(revenue)}\n")
      text_file.write(f"Average Change: ${average}\n")
      text_file.write(f"Greatest Increase In Profits: {dates[max_index]} (${max_value})\n")
      text_file.write(f"Greatest Decrease In Profits: {dates[min_index]} (${min_value})\n")
    
    #print contents of text file to screen
    with open(output_file, "r") as txtfile:
      contents = txtfile.read()
      print(f"\n{contents}")