import os
import csv

# Path to collect data from the folder
budget_data = os.path.join("budget_data.csv")

# Assign values to variables with descriptive names
total_months = 0
profit_loss = 0
change = 0
amount = 0
dates = []
profit = []

# Open and read the CSV file
with open(budget_data, newline = "") as f:
    csvreader = csv.reader(f, delimiter = ",", quoting=csv.QUOTE_NONE)
    csv_header = next(csvreader)

# Looping through the data, tracking total months and total profit/losses
    for row in csvreader:

        # Tracking Dates
        dates.append(row[0])

        # Calculate change in profit
        change = int(row[1])-amount
        profit.append(change)
        amount = int(row[1])
    
        total_months += 1

        profit_loss = profit_loss + int(row[1])

# Finding greatest increase in profits
    greatest_gain = max(profit)
    greatest_list = profit.index(greatest_gain)
    greatest_date = dates[greatest_dict]

# Finding greatest decrease in profits
    worst_loss = min(profit)
    worst_list = profit.index(worst_loss)
    worst_date = dates[worst_dict]

# The average of the changes in "Profit/Losses" over the entire period
# ORIGINAL CODE
    # def average(change):
    #length = len(numbers)
    #total = 0.0
    #for number in numbers:
     #   total += number
    #return total / length

#settled on
    avg_change = sum(profit)/len(profit)

# Printing the information
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_gain)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(worst_loss)})")

# Exporing to text file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_gain)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(worst_loss)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))