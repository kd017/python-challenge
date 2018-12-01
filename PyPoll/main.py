import csv
import os

# Create input path; Assumes the program is executed from PyPoll directory
input_path = os.path.join('Resources', 'election_data.csv')

# Open the file
with open(input_path, 'r') as input_file:

    # Create a CSV reder
    csvreader = csv.reader(input_file)

    # Skip the Header
    header = next(csvreader)

    # Holders for total votes and per-candidate votes
    total_votes = 0
    candidate_votes = {}

    # Iterate through rows
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        # If we are visiting a candidate for the first time, add an entry in the dictionary
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
winner = None
winner_votes = 0
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
    print(f'{candidate}: {votes*100/total_votes:.3f}% ({votes})')

print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

with open('results.txt', 'w') as output_file:
    output_file.write(f'Election Results\n')
    output_file.write(f'-------------------------\n')
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write(f'-------------------------\n')
    winner = None
    winner_votes = 0
    for candidate, votes in candidate_votes.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
        output_file.write(f'{candidate}: {votes*100/total_votes:.3f}% ({votes})\n')

    output_file.write(f'-------------------------\n')
    output_file.write(f'Winner: {winner}\n')
    output_file.write(f'-------------------------\n')