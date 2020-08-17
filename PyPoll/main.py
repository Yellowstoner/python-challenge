import os
import csv

election_data = os.path.join("election_data.csv")

candidates = []
total_votes = 0
candidate_votes = []
percent_votes = []

with open(election_data, newline = "") as f:

    csvreader = csv.reader(f, delimiter = ",", quoting=csv.QUOTE_NONE)
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_list = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            candidate_list = candidates.index(row[2])
            candidate_votes[candidate_list] += 1

    for votes in candidate_votes:
        percent = (votes/total_votes) * 100
        precent = round(percent)
        percent = "%.3f%%" % percent
        percent_votes.append(percent)

    win = max(candidate_votes)
    chicken_dinner = candidate_votes.index(win)
    winner = candidates[chicken_dinner]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


output = open("output.txt", "w")

line1 = "Election Results"
line2 = ("--------------------------")
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = ("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))