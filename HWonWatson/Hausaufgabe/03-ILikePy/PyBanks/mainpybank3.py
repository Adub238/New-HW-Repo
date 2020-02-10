import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

#Define variables
total_months = 0
net_gain = 0
avg_gain = 0
max_gain = None
max_month = None
min_gain = None
min_month = None

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

def show_me_the_stats(bank_data):
    date = str(bank_data[0])
    net_gain = int(bank_data[1])

with open(pybank_csv) as bank_data:
    reader = csv.reader(bank_data)
    header = next (bank_data)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    net_gain = net_gain + int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
            total_months = total_months + 1
            gain = int(row[1])
            net_gain = net_gain + gain
            if max_gain is None:
                max_gain = gain
                max_month = row[0]
                min_gain = gain
                min_month = row[0]
            if max_gain < gain:
                max_gain = gain
                max_month = row[0] #current month
            if min_gain > gain:
                min_gain = gain
                min_month = row[0] #current month

fout = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_gain}
Average  Change: ${net_gain / total_months}
Greatest Increase in Profits: {max_month} [${max_gain}]
Greatest Decrease in Profits: {min_month} [${min_gain}]
"""

print (fout) 
output_path = os.path.join("..", "Analysis", "bank_analysis.txt")
with open(output_path, 'w') as txtfile:
	txtfile.write(fout)
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
