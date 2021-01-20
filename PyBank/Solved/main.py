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

    for row in csv_reader:

        total_months = total_months + 1
        date.append(row[1])

        total_revenue = total_revenue + int(row[1])
        revenue.append(row[1])




print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + str(total_revenue))