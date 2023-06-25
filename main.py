import os
import csv


budgetinfo_csv = os.path.join("C:\\Users\\jerem\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# data to put in lists

date = []
prof_loss = []
month_total = []
prof_loss_total = []
greatInc = []
greatLoss = []

#with open(udemy_csv, encoding='utf-8') as csvfile:
with open(budgetinfo_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csv.reader:

        date.append(row[0])
        prof_loss.append(row[1])

        #total = sum(row[0])
        #month_total.append(str(total))
        #pftotal = sum(row(1))
        #prof_loss_total.append(str(pftotal))


print("Financial Analysis")
print("-----------------------------------------------------------------")
print("Total months: " + 'total' + " ")
print( "Total:  $ " + 'pftotal' + " ")

# output_file = os.path.join("budget_final.md")