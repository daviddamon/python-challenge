#Pypoll

#OUTPUT SAMPLE
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
total_votes = 0

# create lists to store data
unique_candidate_name = []
candidate_votes = []
percent_votes = []


# set path for data file
csvpath = os.path.join('Resources', 'election_data.csv')

# open the CSV
with open(csvpath, 'r') as csvfile:
  reader = csv.DictReader(csvfile, delimiter=',')

  # read the header row and print as check
  csv_header = next(reader)
  print(f"Header: {csv_header}")

  # read each row of data file after header
  for row in reader:

    # print a few rows of dictionary to check
    #if i < 3
      #print row
      #i += 1

    candidate = row["Candidate"]

    total_votes = len(candidate)

    
    # find all candidate names and create new list

    unique_candidate_name.append(set(candidate))

    # just a check of names
    print("Unique Candidate Names: ",unique_candidate_name)

    # count votes per candidate
    candidate_votes = unique_candidate_name.count

    # calculate percentage of votes per candidate
    percent_votes = round((candidate_votes/total_votes)*100,3)



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
print(f'Total Votes: {total_votes}')
print('-------------------------')

for 
  
  print(f'{unique_candidate_name}: {percent_votes}%  ({candidate_votes})')


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