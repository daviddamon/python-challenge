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
kahn_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# create lists to store data
winner = []

# set path for data file
csvpath = os.path.join('Resources', 'test_data.csv')

# open the CSV file and set delimeter (optional with commas)
with open(csvpath, 'r') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')

     # read csv header and skip to first line of data
     csv_header = next(csvreader)
     print(f"Header: {csv_header}")

     # begin loop to read each row of data file after header
     for row in csvreader:
          print(row)

          # increment total vote count
          total_votes += 1
          print(total_votes) 

          if row[2] == "Kahn"
               kahn_votes += 1

          elif row[2] == "Correy"
               correy_votes += 1

          elif row[2] == "Li"
               li_votes += 1

          elif row[2] == "O'Tooley"
               otooley_votes += 1

          else

          print("Kahn:  " + kahn_votes)
          print("Correy:  " + correy_votes)
          print("Li:  " + li_votes)
          print("O'Tooley:  " + otooley_votes)

     # check for winner
     if kahn_votes > (correy_votes and li_votes and otooley_votes)
          winner = "Kahn"

          elif correy_votes > (li_votes and otooley_votes and kahn_votes)
          winner = "Correy"

          elif li_votes > (otooley_votes and kahn_votes and correy_votes)
          winner = "Li"

          elif otooley_votes > (kahn_votes and correy_votes and li_votes)
          winner = "O'Tooley"
     
     else

     print(winner)



# print to terminal
print('Election Results') 
print('----------------------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------------------')
print('Kahn: ' + round(kahn_votes / total_votes * 100,3) + '%  (' + kahn_votes + ')'
print('Correy: ' + round(correy_votes / total_votes * 100,3) + '%  (' + correy_votes + ')'
print('Li: ' + round(li_votes / total_votes * 100,3) + '%  (' + li_votes + ')'
print('O\'Tooley: ' + round(otooley_votes / total_votes * 100,3) + '%  (' + otooley_votes + ')'
print('----------------------------------------')
print(f'Winner: {winner}')
print('----------------------------------------')

# write new text document in different directory
# set destination file path
#filepath = os.path.join('..', 'Analysis')

# create a text file in Analysis folder  
filename = 'Analysis/Pypoll_results.txt'
with open(filename, 'w') as output:

     output.write('Election Results') 
     output.write('----------------------------------------')
     output.write(f'Total Votes: {total_votes}')
     output.write('----------------------------------------')
     output.write('Kahn: ' + round(kahn_votes / total_votes * 100,3) + '%  (' + kahn_votes + ')'
     output.write('Correy: ' + round(correy_votes / total_votes * 100,3) + '%  (' + correy_votes + ')'
     output.write('Li: ' + round(li_votes / total_votes * 100,3) + '%  (' + li_votes + ')'
     output.write('O\'Tooley: ' + round(otooley_votes / total_votes * 100,3) + '%  (' + otooley_votes + ')'
     output.write('----------------------------------------')
     output.write(f'Winner: {winner}')
     output.write('----------------------------------------')
    