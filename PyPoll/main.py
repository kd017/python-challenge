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

    total_votes = 0
    cadndidate_votes = {}

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in cadndidate_votes:
            cadndidate_votes[candidate] = 1
        else:
            cadndidate_votes[candidate] += 1

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
winner = None
winner_votes = 0
for candidate, votes in cadndidate_votes.items():
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
    for candidate, votes in cadndidate_votes.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
        output_file.write(f'{candidate}: {votes*100/total_votes:.3f}% ({votes})\n')

    output_file.write(f'-------------------------\n')
    output_file.write(f'Winner: {winner}\n')
    output_file.write(f'-------------------------\n')