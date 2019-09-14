import os
import csv
PyPoll_data = os.path.join('..', 'election_data.csv')
with open (PyPoll_data, newline='') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    voter_id=[]
    county=[]
    candidate=[]
    for row in csv_file:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#print (voter_id)
#print (county)
#print (candidate)

#PART 1
voter_id_count= len(voter_id)
#print(voter_id_count)

#PART 2
votes = 0
unique_candidates= set()
PyPoll_data = os.path.join('..', 'election_data.csv')
with open (PyPoll_data, newline='') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csv_file:
        unique_candidates.add(row[2])
    #print(unique_candidates)

#PART 3-4
votes = 0
num_votes=[]
list_cand= []
PyPoll_data = os.path.join('..', 'election_data.csv')
with open (PyPoll_data, newline='') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csv_file:
        list_cand.append(row[2])
    #print(list_cand)

khan_total = []
li_total = []
tooley_total = []
correy_total = []

for i in list_cand:
    if i == "Khan":
        khan_total.append(i)
    elif i == "Correy":
        correy_total.append(i)
    elif i == "O'Tooley":
        tooley_total.append(i)
    elif i == "Li":
        li_total.append(i)
khan_final=len(khan_total)
li_final=len(li_total)
tooley_final=len(tooley_total)
correy_final=len(correy_total)

#print(khan_final)
#print(li_final)
#print(tooley_final)
#print(correy_final)

khan_1= int(khan_final)/int(voter_id_count)
khan_percent= khan_1*100
li_1= int(li_final)/int(voter_id_count)
li_percent= li_1*100
tooley_1= int(tooley_final)/int(voter_id_count)
tooley_percent= tooley_1*100
correy_1=int(correy_final)/int(voter_id_count)
correy_percent= correy_1*100

#print(khan_percent)
#print(li_percent)
#print(tooley_percent)
#print(correy_percent)

#PART 5
cand_full= {(khan_final,'Khan'),(li_final,'Li'),(tooley_final,'OTooley'),(correy_final,'Correy')}
winner = max(cand_full)
#print (winner)

print("Election Results")
print("______________________________________________________________________")
print("Total Votes: " + str(voter_id_count))
print("______________________________________________________________________")
print("Khan: " + str(khan_percent)[:4] + "(" +str(khan_final) + ")")
print("Correy: " + str(round(correy_percent,3)) + "(" +str(correy_final) + ")")
print("Li: " + str(round(li_percent,3)) + "(" +str(li_final) + ")")
print("O'Tooley: " + str(round(tooley_percent,3))+ "(" +str(tooley_final) + ")")
print("______________________________________________________________________")
print("Winner: " + str(winner))

with open("outputPyPoll.txt","w") as csv_output:
    output = csv.writer(csv_output, delimiter=",")
    output.writerow(["Election Results"])
    output.writerow(["______________________________________________________________________"])
    output.writerow(["Total Votes: " + str(voter_id_count)])
    output.writerow(["______________________________________________________________________"])
    output.writerow(["Khan: " + str(khan_percent)[:4] + "(" +str(khan_final) + ")"])
    output.writerow(["Correy: " + str(round(correy_percent,3)) + "(" +str(correy_final) + ")"])
    output.writerow(["Li: " + str(round(li_percent,3)) + "(" +str(li_final) + ")"])
    output.writerow(["O'Tooley: " + str(round(tooley_percent,3))+ "(" +str(tooley_final) + ")"])
    output.writerow(["______________________________________________________________________"])
    output.writerow(["Winner: " + str(winner)])
#file.close()