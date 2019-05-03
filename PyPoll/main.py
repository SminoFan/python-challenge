#Brandon Coleman
#Data Analytics
#5-1-2019
#Homework 3 Python Challenge

import csv
import os

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join("output.txt") #output file to be created and written to

votes_dict = {} #dictionary to store candidates key and votes value
key = "" #key variable
Total_Votes = 0 #total votes variable

#get total votes by summing values in dictionary and append to output.txt
def GetTotalVotes(Votes): 
    Total_Votes = sum(Votes.values())
    text_file = open(output_file, "a")
    text_file.write("Election Results\n-------------------------\n")
    text_file.write(f"Total Votes: {Total_Votes}\n-------------------------\n")
    return

#Calculate, format, and append percentage
def GetPercentages(Percentages): 
    Total_Votes = sum(Percentages.values())
    textfile = open(output_file, "a")
    for key in Percentages:    
        voteshare = (Percentages[key] / Total_Votes)*100
        voteshare = "{:.3f}%".format(round(voteshare,2))
        textfile.write(f"{key}: {voteshare} ({Percentages[key]})\n")
    textfile.write("-------------------------\n")    
    return

#Get max value from dictionary and write to output.txt
def GetWinner(Winner):
    txtfile = open(output_file, "a")
    txtfile.write(f"Winner: {max(Winner, key=Winner.get)}\n")
    txtfile.write("-------------------------\n")
    return

#read in CVS file and store into dictionary to be used by various functions
with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    for row in csvreader:
            key = row[2]
            if key in votes_dict:
                votes_dict[row[2]] += 1
            else:
                votes_dict[key] = 1


#Function Calls
GetTotalVotes(votes_dict)
GetPercentages(votes_dict)
GetWinner(votes_dict)

#Print Output.txt contents to terminal
with open(output_file, 'r') as output_text:
    text_contents = output_text.read()
print(f"\n{text_contents}")