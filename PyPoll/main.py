import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Set up lists
total_count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        #counting votes
        total_count = total_count + 1
        #appending list to isolate candidates from third item in list
        candidatelist.append(row[2])
    # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/total_count)*100
        vote_percent.append(z)

        winning_vote_count = max(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]

#print to terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#print to text file
txtpath = os.path.join("Analysis", "Election_resutls_KAL.txt")
with open(txtpath, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")