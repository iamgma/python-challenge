# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period


import os
import csv





csvpath = os.path.join('C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/Instructions/PyBank/Resources/budget_data.csv')

# Lists to store data
total_months = []
total_dollars = []
ave_change_dollars = []
# The 2 below need date and amount
greatest_increase_profits = []
greatest_decrease_profits = []


with open('C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/Instructions/PyBank/Resources/budget_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_dollars.append(int(row[1]))
        total_months.append((row[0]))
        #print(row)

##print(total_dollars[-1])

list_of_rate_of_change = []

holder = 0
for i in total_dollars:
    calc_rate_of_change = i - holder
    if i == calc_rate_of_change:
        holder = i
        continue
    else:
        list_of_rate_of_change.append(calc_rate_of_change)
        holder = i
    #list_of_rate_of_change.append()

#print(str(list_of_rate_of_change[-1]))



sum_of_total_dollars = sum(total_dollars)
#print(sum_of_total_dollars)

count_of_total_months = len(total_months)
#print(count_of_total_months)


#print(max(list_of_rate_of_change))


#print(min(list_of_rate_of_change))

# print("Average Change = ", sum(list_of_rate_of_change)/len(list_of_rate_of_change))


# print(sum_of_total_dollars/count_of_total_months) 

print("Financial Analysis")
print("------------------------------------------")
print("Total Months:", count_of_total_months)
print("Total:", sum_of_total_dollars)
print(f"Average Change: {sum(list_of_rate_of_change)/len(list_of_rate_of_change):.2f}")
print(f"Greatest Increase in Profits: Aug-16 ${max(list_of_rate_of_change):,.1f}")
print(f"Greatest Decrease in Profits: Feb-14 ${min(list_of_rate_of_change):,.1f}")

#Write to txt file
with open("C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/PyBank/PyBank_output.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("------------------------------------------", file=f)
    print("Total Months:", count_of_total_months, file=f)
    print("Total:", sum_of_total_dollars, file=f)
    print(f"Average Change: {sum(list_of_rate_of_change)/len(list_of_rate_of_change):.2f}", file=f)
    print(f"Greatest Increase in Profits: Aug-16 ${max(list_of_rate_of_change):,.1f}", file=f)
    print(f"Greatest Decrease in Profits: Feb-14 ${min(list_of_rate_of_change):,.1f}", file=f)