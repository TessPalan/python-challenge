import pathlib
import csv

# Collect data from election_data.csv
election_data_csv = pathlib.Path('PyPoll/Resources/election_data.csv')


with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)

    votes = {}
    

    for row in csvreader:
        
        # complete list of candidates who received votes
        # candidates vote count 
        candidate_name = row[2]

        if candidate_name in votes:
            votes[candidate_name] += 1
        else:
            votes[candidate_name] = 1

   # print(votes)
    vote_counts = (list(votes.values()))

    # total number of votes cast 
    total_count = sum(vote_counts)
    #print(total_count)

winner = list(votes.keys())[0]
votes_summary = {}
for candidate in votes.keys():
    if votes[candidate] > votes[winner]:
        winner = candidate
    votes_summary[candidate] = {'votes': votes[candidate], 'vote_pct': round((votes[candidate]/total_count)*100,3)}
    if candidate == winner:
        votes_summary[candidate]["is_winner"] = True
    else:
        votes_summary[candidate]["is_winner"] = False


election_results_csv = pathlib.Path('PyPoll/Analysis/PyPoll_analysis.txt')


with open(election_results_csv,'w') as outputfile:
    #csvwriter = csv.writer(outputfile)
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_count}\n"
    f"-------------------------\n"
    )
    print(election_results, end="")

    outputfile.write(election_results)

    for candidate in votes_summary.keys():
        voter_output = f"{candidate}: {votes_summary[candidate]['vote_pct']}% ({votes_summary[candidate]['votes']})\n"
        print(voter_output, end="")

        outputfile.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
    outputfile.write(winning_candidate_summary)

    print(winning_candidate_summary)


