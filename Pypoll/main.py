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
#import collections

# initialize variables
total_votes = 0

# create lists to store data
names = []
votes = []
voting_data = ['1', '2']

# set path for data file
csvpath = os.path.join('Resources', 'test_data.csv')

# open the CSV file and set delimeter (optional with commas)
with open(csvpath, 'r') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')

     print (csvreader)

     # read the header row first
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")  

     # begin loop to read each row of data file after header
     for row in csvreader:
          print(row)

          # increment total vote count
          total_votes += 1

          name = row[1]
          vote = row[2]

          # loop to add names and votes to running total
          if name in names:
               name_index = names.index(name)
               votes[name_index] = votes[name_index] + 1

          else:
               names.append(name)
               votes.append(vote)

     # declare more variables for next loop
     percent = []
     highest = vote[0]
     highest_index = 0

     # calculate percentage and winner
     for count in range(len(name)):
          vote_percent = vote[count]/total_votes*100
          percent.append(vote_percent)

     if vote[count] > highest:
          highest = vote[count]
          print(highest)
          highest_index = count

     # declare winner 
     win_name = names[highest_index]
   
     # calculate percentage of votes
     percent = [round(i,3) for i in percent]
    
     ##################################################################

     # find all candidate names and create new list

     #unique_name.append(set(candidate))

     # count votes per candidate
     #candidate_votes = unique_candidate_name.count

     #print counts #prints list with counts for eack
     #x = list(counts.elements())
     #print x

     #y = counts.most_common(2)  # counts top two winners
     #print y[1]  # prints top winner only

     #winner = unique_candidate_name[candidate_votes.index(max(candidate_votes))]


     #######################################################

#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

# print to terminal

print('Election Results') 
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

for count in range(len(name)):
     print(f'{name[count]}: {percent[count]}%  ({votes[count]})')

print('-------------------------')
print(f'Winner: {win_name}')
print('-------------------------')


# write new text document
# set destination file path
txtpath = os.path.join('..', 'Analysis')

# create a text file in Analysis folder  
filename = ('txtpath', 'vote_summary.txt')
with open(filename, 'w') as output:

     output.write('Election Results')
     output.write('-------------------------')
     output.write(f'Total Votes: {total_votes}')
     output.write('-------------------------')

     for count in range(len(name)):
          output.write(f'{name[count]}: {percent[count]}%  ({votes[count]})')

     output.write('-------------------------')
     output.write(f'Winner: {win_name}')
     output.write('-------------------------')
 