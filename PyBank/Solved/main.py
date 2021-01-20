import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    file_output = "budget_analysis.txt"
    


    total_revenue = 0
    total_months = 0
    revenue_length = 0   
    avg_revenue_change = 0
    max_revenue_change = 0
    min_revenue_change = 0
    max_revenue_change_date = None
    min_revenue_change_date = None
    revenue = []
    revenue_change = []
    date = []

#calculating the total months and revenue
    for row in csv_reader:

        total_months = total_months + 1
        date.append(row[0])

        total_revenue = total_revenue + int(row[1])
        revenue.append(row[1])


#printing the first part of the assignment

print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))

#finding the average, max, and minimum changes

for i in range(len(revenue)-1):
    change = int(revenue[i+1]) - int(revenue[i])
    revenue_change.append(change)

avg_revenue_change = round(sum(revenue_change)/len(revenue_change), 2)
    
max_revenue_change = round(max(revenue_change),2)
max_revenue_change_date = str(date[revenue_change.index(max(revenue_change)) +1])
    
min_revenue_change = round(min(revenue_change),2)
min_revenue_change_date = str(date[revenue_change.index(min(revenue_change)) +1])

#printing the remainder of the assignment

print("Average Revenue Change: $" + str(avg_revenue_change))
print("Greatest Increase in Profits: " + str(max_revenue_change_date) + "($" + str(max_revenue_change) +")")
print("Greatest Decrease in Profits: " + str(min_revenue_change_date) + "($" + str(min_revenue_change) +")")


#send to txt file

with open(file_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(avg_revenue_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(max_revenue_change_date)+ " ($" + str(max_revenue_change) +")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(min_revenue_change_date)+ " ($" + str(min_revenue_change)+")")