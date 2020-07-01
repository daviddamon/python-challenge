#Pypoll

#Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------

  ###########################################

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