
## PyPoll

#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#import systems

import os
import csv

#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#pull CSV file, get header
pypolls_csv = os.path.join("Resources","election_data.csv")

with open(pypolls_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

#assign necessary variables
total_votes_cast = 0
candidate_dict = {}

#start the functioning
with open(pypolls_csv) as polling_data:
    reader = csv.reader(polling_data)
    header = next (polling_data)
    #A complete list of candidates who received votes--->repeating loop that filters through list adding new candidates to list???
    for row in reader:
        total_votes_cast += 1
        name = row[2]
        if name in candidate_dict:
          candidate_dict[name] += 1
        else:
          candidate_dict[name] = 1
   
khan_votes=candidate_dict["Khan"]
khan_percent=khan_votes/total_votes_cast *100
correy_votes=candidate_dict["Correy"]
correy_percent=correy_votes/total_votes_cast*100
li_votes=candidate_dict['Li']
li_percent=li_votes/total_votes_cast*100
tooley_votes=candidate_dict["O'Tooley"]
tooley_percent=tooley_votes/total_votes_cast*100

print (total_votes_cast)
print(candidate_dict)


fstring = f"""
Election Results
----------------------------
Total Votes Cast : {total_votes_cast}
---------------------------
Results :
Khan: {khan_votes}, {khan_percent} %
Correy: {correy_votes}, {correy_percent} %
Li: {li_votes}, {li_percent} %
O'Tooley: {tooley_votes}, {tooley_percent} %
--------------------------
Winner: Khaaan!!!
--------------------------
"""
print(fstring)
output_path = os.path.join("..", "Analysis", "polls_analysis.txt")
with open(output_path, 'w') as txtfile:
	txtfile.write(fstring)
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
