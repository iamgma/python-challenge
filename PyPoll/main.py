# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process. 
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
            # * The total number of votes cast
            # * A complete list of candidates who received votes
            # * The percentage of votes each candidate won
            # * The total number of votes each candidate won
            # * The winner of the election based on popular vote.


import os
import csv


csvpath = os.path.join('C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/Instructions/PyPoll/Resources/election_data.csv')

# Lists to store data
total_votes = []
list_candidates_who_got_votes = []
# Need percent votes each candidate won
percent_votes = []
# Need total number of votes for each candidate
total_votes_candidate = []
pop_vote_winner = []

Diana_DeGette_votes = []
Charles_Casper_Stockham_votes = []
Raymon_Anthony_Doane_votes = []


with open('C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/Instructions/PyPoll/Resources/election_data.csv') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #this is a for loop
    # this is will loop through EVERY 'x' in csvreader
    # each 'x' is a a python list
    # this 'x' can be thought of as a row in a spreadsheet
    for x in csvreader:
        # this will append x[0], aka column 0 in row x
        # this will append to 'total_votes'
        total_votes.append(x[0])
        # this will append x[2], column 2 in row x
        # this will append to "list_candidates_who_got_votes"
        list_candidates_who_got_votes.append(x[2])

        #this is a conditional
        #this tells us that if the value in row x column 2 is equal to "Diana DeGette"
        #this will append x[0] to Diana_DeGette_votes
        if x[2] == "Diana DeGette":
            Diana_DeGette_votes.append(x[0])
        #this tells us that if the value in row x column 2 is equal to "Charles Casper Stockham"
        #this will append x[0] to Charles_Casper_Stockham_votes
        elif x[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes.append(x[0])
        #this tells us that if the value in row x column 2 is equal to "Raymon Anthony Doane"
        #this will append x[0] to Raymon_Anthony_Doane_votes
        else:
            Raymon_Anthony_Doane_votes.append(x[0])
  

count_of_votes_cast = len(total_votes)
#print(count_of_votes_cast)

unique_list_candidates = set(list_candidates_who_got_votes)
#print(unique_list_candidates)

#This variable gets us the length of the list Diana DeGette votes
#The length of the list gives us the count of the voter ids that we added in line 54,55
count_of_votes_for_Diana = len(Diana_DeGette_votes)
#print(count_of_votes_for_Diana)

count_of_votes_for_Charles = len(Charles_Casper_Stockham_votes)
count_of_votes_for_Raymon = len(Raymon_Anthony_Doane_votes)

#To find the percent of votes Diana got
#Take total_votes and divide by Diana votes
print('/n')
print("Election Results")
print("-----------------------")
print(f"Total Votes: {count_of_votes_cast}")
print("-----------------------")
print(f"Diana DeGette: {count_of_votes_for_Diana/count_of_votes_cast:.1%} ({count_of_votes_for_Diana})")
print(f"Charles Casper Stockham: {count_of_votes_for_Charles/count_of_votes_cast:.1%} ({count_of_votes_for_Charles})")
print(f"Raymon Anthony Doane: {count_of_votes_for_Raymon/count_of_votes_cast:.1%} ({count_of_votes_for_Raymon})")
print("-----------------------")
print("Winner: Diana DeGette")

#Write to txt file
with open("C:/Users/gmass/Documents/UC_Berk_Bootcamp/Python-Challenge/PyPoll/PyPoll_output.txt", "w") as f:
    print("Election Results", file=f)
    print("-----------------------", file=f)
    print(f"Total Votes: {count_of_votes_cast}", file=f)
    print("-----------------------", file=f)
    print(f"Diana DeGette: {count_of_votes_for_Diana/count_of_votes_cast:.1%} ({count_of_votes_for_Diana})", file=f)
    print(f"Charles Casper Stockham: {count_of_votes_for_Charles/count_of_votes_cast:.1%} ({count_of_votes_for_Charles})", file=f)
    print(f"Raymon Anthony Doane: {count_of_votes_for_Raymon/count_of_votes_cast:.1%} ({count_of_votes_for_Raymon})", file=f)
    print("-----------------------", file=f)
    print("Winner: Diana DeGette", file=f)