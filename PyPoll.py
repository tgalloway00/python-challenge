import os
import csv

total_votes = []
candidate_list = []
unique_candidate = []
average_change = []
candidate_votes = []
percentage = []

# pull data from particular csv
csvpath = os.path.join('election_data.csv')
with open(csvpath) as election_data:
    election_reader = csv.reader(election_data, delimiter=',')
    # skip over header
    next(election_reader)

    # start for loop to get list of voters and list of candidates
    for row in election_reader:
        candidate_list.append(str(row[2]))
        total_votes.append(row[0])
    # loop to find unique candidates
    for x in candidate_list:
        if x not in unique_candidate:
            unique_candidate.append(x)

    # loop to find number of votes per candidate
    for i in unique_candidate:
        candidate_votes.append(candidate_list.count(i))
    # loop through candidate votes to calculate the rounded percentage of votes per person
    for j in candidate_votes:
        percentage.append(round(((int(j) / (len(total_votes))) * 100), 3))

# Print all values
print("Election Results")
print("----------------------")
print(f"Total Votes: {len(total_votes)}")
print("----------------------")
for f in range(len(unique_candidate)):
    print(unique_candidate[f] + ":" + " " + str(percentage[f]
          ) + "%" + " " + "("+str(candidate_votes[f])+")")
print("----------------------")

zipped = zip(candidate_votes, unique_candidate)
zipped = set(zipped)
max = max(zipped)
print(f"Winner: {max[1]}")
print("----------------------")

output_path = os.path.join("..", "python-challenge", "pypoll.csv")
with open(output_path, 'w') as csvfile:
    election_reader = csv.writer(election_data, delimiter=',')

    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------"])
    csvwriter.writerow(["Total Votes: " + str(len(total_votes))])
    csvwriter.writerow(["----------------------"])
    for f in range(len(unique_candidate)):
        csvwriter.writerow([unique_candidate[f] + ":" + " " + str(percentage[f]
          ) + "%" + " " + "("+str(candidate_votes[f])+")"])
    csvwriter.writerow(["----------------------"])
    csvwriter.writerow(["Winner:" + str(max[1])])
    csvwriter.writerow(["----------------------"])