#Pypoll

#OUTPUT
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

# initialize variables
vote_count = 0


# headers in csv file
VoterID
County
Candidate

# set path for data file
csvpath = os.path.join('Resources', 'election_data.csv')

# open the CSV
with open(csvpath, newline='') as csvfile:
  csv_reader = csv.DictReader(csvfile, delimiter=',')

  # print csv contents as check
  # print(csv_reader)

    # read the header row and print as check
    #csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # read each row of data file after header
    for row in csv_reader:

        print(row) # another row check to be commented out later

       

# print to terminal


#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

print('Election Results') 
print('-------------------------')
print(f'Total Votes: {vote_count}')
print('-------------------------')

for 
  candidate_percent = round(candidate_votes/vote_count,3)
  print(f'{candidate_name}: {candidate_percent}%  ({candidate_vote})')


# write new text document
# set destination file path
txtpath = os.path.join('..', 'Analysis')

# create a text file in Analysis folder  
filename = 'txtpath/vote_summary.txt'
with open(filename, 'w') as output:

  output.write('Election Results') 
  output.write('-------------------------')
  output.write(f'Total Votes: {vote_count}')
  output.write('-------------------------')
  output.write
  output.write
  output.write
  output.write