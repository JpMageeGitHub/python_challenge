import os
import csv

# Grab file for reading 
pollinfo = os.path.join("Resources", "election_data.csv").replace("\\","/")

# Making lists

voterid = []
county = []
candidate = []

# Read and strip data into lists

with open(pollinfo) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    counter = 0
    total_vote = 0
    totalchange = 0
    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        Totalcast = len(voterid)
        
# Find number of votes and percentages for each candidate
        
charles = candidate.count("Charles Casper Stockham")
diana = candidate.count("Diana DeGette")
raymon = candidate.count("Raymon Anthony Doane")

perCharles = round((charles / Totalcast) * 100, 3)
perDiana = round((diana / Totalcast) * 100, 3)
perRaymon = round((raymon / Totalcast) * 100, 3) 

# Let's find the winner

candidates = [charles, diana, raymon]

winner = max(candidates)

if winner == charles:
   v = ' Charles Casper Stockham'
elif winner == diana:
    v = ' Diana DeGette'
else:
    v = ' Raymon Anthony Doane' 

#Print the output to the Terminal

print("Election Results: ")
print("--------------------------------------")
print("Total Votes: " + str(Totalcast))
print('--------------------------------------')
print("Charles Casper Stockham: " + str(perCharles) + "%   "+  "(" +  str(charles) + ") votes")
print("Diana DeGette:           " + str(perDiana) + "%   " + "(" + str(diana) + ")  votes")
print("Raymon Anthony Doane:    " + str(perRaymon) + "%   " + " (" + str(raymon) + ") votes")
print("--------------------------------------")
print("Winner: " + v)
print("--------------------------------------")

#Print the output to a text file
with open("poll_final.txt", "w") as datafile:
    print("Election Results: ", file = datafile)
    print("--------------------------------------", file = datafile)
    print("Total Votes: " + str(Totalcast), file = datafile)
    print('--------------------------------------', file = datafile)
    print("Charles Casper Stockham: " + str(perCharles) + "%   "+  "(" +  str(charles) + ") votes", file = datafile)
    print("Diana DeGette:           " + str(perDiana) + "%   " + "(" + str(diana) + ")  votes", file = datafile)
    print("Raymon Anthony Doane:    " + str(perRaymon) + "%   " + " (" + str(raymon) + ") votes", file = datafile)
    print("--------------------------------------", file = datafile)
    print("Winner: " + v, file = datafile)
    print("--------------------------------------", file = datafile)
datafile.close()