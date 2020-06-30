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

# create profit and loss variables
maxprof = 0
maxloss = 0
rowcount = 0

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
        TPL = TPL + row[1]

        # record maximum profit
        if row[1] > maxprof
            row[1] = maxprof
            row[0] = maxdate

        # record maximum loss
        if row[1] < maxloss
            row[1] = maxloss
            row[0] = mindate

    # print to terminal
    print(f"Total Months: "{rowcount -1})

    print(f"Total: $"{TPL})

    print (f"Greatest Increase in Profits: "{maxdate}"  ($"{maxprof}")")

    print (f"Greatest Decrease in Profits: "{mindate}"  ($"{maxloss}")")
           
    # export a text file to Analysis folder
    