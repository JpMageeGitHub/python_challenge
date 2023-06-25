import os
import csv

# Call the file to read

budgetinfo = os.path.join("Resources", "budget_data.csv").replace("\\","/")

# data to put in lists

date = []
profit = []
prof_change = []
 
#Read the file and strip pertinent information

with open(budgetinfo) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    counter = 0
    total_profit = 1088983
    totalchange = 0
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        Total_months = len(date)
     # Use counter to calculate profit change   
        if counter > 0:

            counterlast = counter - 1
            counternext = counter + 1
            calc = int(profit[counter]) - int(profit[counterlast])
            prof_change.append(calc)
            total_profit = total_profit + int(profit[counter])
            totalchange = totalchange + int(prof_change[counterlast])
        counter = counter + 1

# Calculate and find the necessary varaibles to print

avg_change = totalchange / 85 
avg_change = round(avg_change, 2)
maxchange = max(prof_change)
maxpos = ((prof_change.index(maxchange)) + 1)
maxdate = date[int(maxpos)]
minchange = min(prof_change)
minpos = ((prof_change.index(minchange)) + 1)
mindate = date[int(minpos)]        

# Print outputs to Terminal
        
print("Financial Analysis")
print("-----------------------------------------------------------------")
print("Total months: " + str(Total_months))
print("Total profit: $" + str(total_profit))
print("Average change: $" + str(avg_change))
print("Greatest increase: " + str(maxdate)  + "  $" + str(maxchange))
print("Greatest decrease: " + str(mindate) + "  $" + str(minchange))



#  Open and print to the output file
with open("budget_final.txt", "w") as datafile:
    print("Financial Analysis", file = datafile)
    print("-----------------------------------------------------------------", file = datafile)
    print("Total months: " + str(Total_months), file = datafile)
    print("Total profit: $" + str(total_profit), file = datafile)
    print("Average change: $" + str(avg_change), file = datafile)
    print("Greatest increase: " + str(maxdate)  + "  $" + str(maxchange), file = datafile)
    print("Greatest decrease: " + str(mindate) + "  $" + str(minchange), file = datafile)
    datafile.close()
