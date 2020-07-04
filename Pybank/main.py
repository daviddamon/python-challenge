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
max_profit_date = 0
max_loss_date = 0
month_count = 0

# set path for data file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open the CSV
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # print csv contents as check
    print(csv_reader)

    # read the header row and print as check
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # read each row of data file after header
    for row in csv_reader:

        print(row) # another row check to be commented out later

        date = row[0]
        profit = int(row[1])

        # increment month counter
        month_count += 1
        
        # calculate total profit or loss
        total_profit_loss = total_profit_loss + profit

        # record maximum profit
        if profit > max_profit:
            max_profit = profit
            max_profit_date = date
     
        # record maximum loss
        if profit < max_loss:
            max_loss = profit
            max_loss_date = date

# print to terminal
print(f'Total Months: {month_count}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${round(total_profit_loss/month_count,2)}')
print(f'Greatest Increase in Profits: {max_profit_date}  (${max_profit})')
print(f'Greatest Decrease in Profits: {max_loss_date}  (${max_loss})')

# write new text document
# set destination file path
txtpath = os.path.join('..', 'Analysis')

# create a text file in Analysis folder  
filename = 'summary.txt'
with open(filename, 'w') as output:

    output.write(f'Total Months: {month_count}\n')
    output.write(f'Total: ${total_profit_loss}\n')
    output.write(f'Average Change: ${round(total_profit_loss/month_count,2)}\n')
    output.write(f'Greatest Increase in Profits: {max_profit_date}  (${max_profit})\n')
    output.write(f'Greatest Decrease in Profits: {max_loss_date}  (${max_loss})\n')
