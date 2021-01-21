
import os
import csv

filepath = os.path.join( "..",'Resources','election_data.csv')
file_output = "Election_results.txt"

#defining numerous variables

totalcount = 0; 
Khancount = 0; 
Correycount = 0; 
Licount = 0; 
OTooleycount = 0; 
max_votecount = 0

def percentage (part, whole):
    return round(100 * float(part)/float(whole),3)

#counting the vote 

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         county = i[1]
         candidate = i[2]
        
         totalcount = totalcount + 1

        
         if candidate =="Khan":
            Khancount = Khancount + 1

         if candidate =="Correy":
            Correycount = Correycount + 1

         if candidate =="Li":
            Licount = Licount + 1

         if candidate =="O'Tooley":
            OTooleycount = OTooleycount + 1
            
#finding the winner
     candidatevote = {"Khan": Khancount,"Correy": Correycount,"Li" :Licount, "O'Tooley": OTooleycount}

     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate

# Display results       

results =(
    print("Election Results"),
    print("-------------------------------"),
    print("Total Votes: " + str(totalcount)),
    print("-------------------------------"),

    print("Khan: " + str(percentage(Khancount,totalcount)) + "% " +  "(" + str(Khancount) + ")"),
    print("Correy: " + str(percentage(Correycount,totalcount)) + "% " + "(" + str(Correycount) +")"),
    print("Li: " + str(percentage(Licount,totalcount)) + "% " + "(" + str(Licount) + ")"),
    print("O'Tooley: " + str(percentage(OTooleycount,totalcount)) + "% " + "(" + str(OTooleycount) + ")"),
    print("--------------------------------"),
    print("Winner: " + str(winner)),
    print("--------------------------------"))



#send to txt file

with open(file_output, "w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("-------------------------------")
    text_file.write("\n")
    text_file.write("Total Votes: " + str(totalcount))
    text_file.write("\n")
    text_file.write("-------------------------------")
    text_file.write("\n")
    text_file.write("Khan: " + str(percentage(Khancount,totalcount)) + "% " +  "(" + str(Khancount) + ")")
    text_file.write("\n")
    text_file.write("Correy: " + str(percentage(Correycount,totalcount)) + "% " + "(" + str(Correycount) +")")
    text_file.write("\n")
    text_file.write("Li: " + str(percentage(Licount,totalcount)) + "% " + "(" + str(Licount) + ")")
    text_file.write("\n")
    text_file.write("O'Tooley: " + str(percentage(OTooleycount,totalcount)) + "% " + "(" + str(OTooleycount) + ")")
    text_file.write("\n")
    text_file.write("--------------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + str(winner))
    text_file.write("\n")
    text_file.write("--------------------------------")