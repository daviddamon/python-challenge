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
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through to analyze data
    for row in csvreader:

        # count number of rows
        rowcount += 1

        # calculate total profit or loss
        TPL = TPL + int(row[1])

        # record maximum profit
        if row[1] > maxprofit
            maxprofit = int(row[1]) and maxdate = str(row[0])

        # record maximum loss
        if row[1] < maxloss
            maxloss = int(row[1]) and mindate = str(row[0])

    # calculate months
    months = rowcount - 1

    # print to terminal
    print(f"Total Months: "{months})

    print(f"Total: $"{TPL})

    print(f"Average Change: $"{float(TPL/months)})

    print (f"Greatest Increase in Profits: "{maxdate}"  ($"{maxprofit}")")

    print (f"Greatest Decrease in Profits: "{mindate}"  ($"{maxloss}")")
           
    # export a text file to Analysis folder
    