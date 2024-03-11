import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

#Set up lists
date = []
profit = []
profit_change = []

#Set initial count for lists
month_count = 0
total_profit = 0
profit_ini = 0
total_profit_change = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        #counting months
        month_count = month_count + 1
        #appending list to isolate months 
        date.append(row[0])
        #appending list to isolate profit and calculate total profit and average change
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        #monthly average change calculation
        end_profit = int(row[1])
        monthly_profit_change = end_profit - profit_ini
        #Store profit change in list
        profit_change.append(monthly_profit_change)
        total_profit_change = total_profit_change + monthly_profit_change
        profit_ini = end_profit

        #calculate average change overall
        average_profit_change = (total_profit_change/month_count)

        #greatest increase and decrease calc
        greatest_inc_profit = max(profit_change)
        greatest_dec_profit = min(profit_change)

        date_inc = date[profit_change.index(greatest_inc_profit)]
        date_dec = date[profit_change.index(greatest_dec_profit)]

#Print in terminal
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(month_count))
print("Total Profits " + "$" + str(total_profit))
print("Average Change " + str(int(average_profit_change)))
print("Greatest Increase in Profits: " + str(date_inc) + " ($" + str(greatest_inc_profit) + ")")
print("Greatest Decrease in Profits: " + str(date_dec) + " ($" + str(greatest_dec_profit) + ")")

txtpath = os.path.join("Analysis", "Financial_Analysis_KAL.txt")
with open(txtpath, "w") as text:
    
    text.write("Financial Analysis"+ "\n")
    text.write("-----------------------------\n\n")
    text.write("Total Months: " + str(month_count) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("Average Change: " + "$" + str(int(average_profit_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(date_inc) + " ($" + str(greatest_inc_profit) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(date_dec) + " ($" + str(greatest_dec_profit) + ")\n")