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
vote_count = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# create lists to store data
winner = []

# set path for data file
csvpath = os.path.join('Resources', 'election_data.csv')

# open the CSV file and set delimeter (optional with commas)
with open(csvpath, 'r') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')

     # read csv header and skip to first line of data
     csv_header = next(csvreader)
     # print(f"Header: {csv_header}")

     # begin loop to read each row of data file after header
     for row in csvreader:
          # print(row)

          # increment total vote count
          vote_count += 1
          # print(vote_count) 

          x = row[2]

          if x == "Khan":
               khan_votes += 1

          elif x == "Correy":
               correy_votes += 1

          elif x == "Li":
               li_votes += 1

          elif x == "O'Tooley":
               otooley_votes += 1

# print to terminal as vote check
# print(f'Khan:  {khan_votes}')
# print(f'Correy:  {correy_votes}')
# print(f'Li:  {li_votes}')
# print(f'O\'Tooley:  {otooley_votes}')

# check for winner
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
     winner = "Khan"

elif correy_votes > li_votes and correy_votes > otooley_votes and correy_votes > khan_votes:
     winner = "Correy"

elif li_votes > otooley_votes and li_votes > khan_votes and li_votes > correy_votes:
     winner = "Li"

elif otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
     winner = "O'Tooley"

# print(winner)

# print to terminal
print('Election Results') 
print('----------------------------------------')
print(f'Total Votes: {vote_count}')
print('----------------------------------------')
print('Khan: ' + f"{khan_votes/vote_count * 100:.3f}" + '%  (' + str(khan_votes) + ')')
print('Correy: ' + f"{correy_votes/vote_count * 100:.3f}" + '%  (' + str(correy_votes) + ')')
print('Li: ' + f"{li_votes/vote_count * 100:.3f}" + '%  (' + str(li_votes) + ')')
print('O\'Tooley: ' + f"{otooley_votes/vote_count * 100:.3f}" + '%  (' + str(otooley_votes) + ')')
print('----------------------------------------')
print(f'Winner: {winner}')
print('----------------------------------------')

# write new text document in different directory
# set destination file path
#filepath = os.path.join('../Analysis/')

# create a text file in Analysis folder  
filename = 'Analysis/Pypoll_results.txt'
with open(filename, 'w') as output:

     output.write('Election Results\n') 
     output.write('----------------------------------------\n')
     output.write(f'Total Votes: {vote_count}\n')
     output.write('----------------------------------------\n')
     output.write('Khan: ' + f"{khan_votes/vote_count * 100:.3f}" + '%  (' + str(khan_votes) + ')\n')
     output.write('Correy: ' + f"{correy_votes/vote_count * 100:.3f}" + '%  (' + str(correy_votes) + ')\n')
     output.write('Li: ' + f"{li_votes/vote_count * 100:.3f}" + '%  (' + str(li_votes) + ')\n')
     output.write('O\'Tooley: ' + f"{otooley_votes/vote_count * 100:.3f}" + '%  (' + str(otooley_votes) + ')\n')
     output.write('----------------------------------------\n')
     output.write(f'Winner: {winner}\n')
     output.write('----------------------------------------\n')
