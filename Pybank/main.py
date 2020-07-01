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
# import datetime # dont need yet - not comparing date

# set variables
rowcount, TPL, maxprofit, maxloss, months = 0

# set path for file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # loop through to create dictionary
    for row in csvreader:

        ledger = ('date': 'row[0]', 'profit': 'row[1]')



    # count number of rows
    num_rows = len(ledger)




    # calculate total profit or loss
    TPL = TPL + int(row[1])

    # record maximum profit
    if row[1] > maxprofit
        maxprofit = int(row[1]) and maxdate = str(row[0])

    # record maximum loss
    if row[1] < maxloss
        maxloss = int(row[1]) and mindate = str(row[0])

    # calculate months
    months = num_rows - 1

    # print to terminal
    print(f"Total Months: "{months})
    print(f"Total: $"{TPL})
    print(f"Average Change: $"{float(TPL/months)})
    print(f"Greatest Increase in Profits: "{maxdate}"  ($"{maxprofit}")")
    print(f"Greatest Decrease in Profits: "{mindate}"  ($"{maxloss}")")



    # set destination file path
    # fix    txtpath = os.path.join('..', 'Analysis', 'summary.txt')

    # create a text file in Analysis folder  
    filename = 'summary.txt'
    with open(filename, 'w') as output:

        output.write(f"Total Months: "{months})
        output.write(f"Total: $"{TPL})
        output.write(f"Average Change: $"{float(TPL/months)})
        output.write(f"Greatest Increase in Profits: "{maxdate}"  ($"{maxprofit}")")
        output.write(f"Greatest Decrease in Profits: "{mindate}"  ($"{maxloss}")")