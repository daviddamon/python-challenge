#Pybank

# OUTPUT
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
###################################################################

# modules
import os
import csv

# initialize variables
total_profit_loss = 0
max_profit = 0
max_loss = 0
months = 0

# set path for file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# open the CSV
with open(csvpath) as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter=',')

    # count number of rows
    months = len(list(csv_dict_reader)) - 1
    print(months)

    # loop through to create dictionary
    for row in csv_dict_reader:

        print(row)

        date = row['Date']
        profit = int(row['Profit/Losses'])

        # calculate total profit or loss
        total_profit_loss = total_profit_loss + profit

        # record maximum profit
        if profit > max_profit:
            max_profit = profit
            max_date = date
     
        # record maximum loss
        if profit < max_loss:
            max_loss = profit
            min_date = date

   

# print to terminal
print(f'Total Months: {months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${float(total_profit_loss/months)}')
print(f'Greatest Increase in Profits: {max_date}  (${max_profit})')
print(f'Greatest Decrease in Profits: {min_date}  (${max_loss})')

# write new text document
# set destination file path
txtpath = os.path.join('..', 'Analysis', 'summary.txt')

# create a text file in Analysis folder  
filename = 'summary.txt'
with open(filename, 'w') as output:

    output.write(f'Total Months: {months}')
    output.write(f'Total: ${total_profit_loss}')
    output.write(f'Average Change: ${float(total_profit_loss/months)}')
    output.write(f'Greatest Increase in Profits: {max_date}  (${max_profit})')
    output.write(f'Greatest Decrease in Profits: {min_date}  (${max_loss})')