import pathlib
import csv

# Collect data from budget_data.csv
budget_data_csv = pathlib.Path('PyBank/Resources/budget_data.csv')

# open and read csv
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months = 1
    total_profitlosses = 0
    previous_profitlosses = 0

    # header row 
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")
    first_row = next(csvreader)
    previous_profitlosses = int(first_row[1])
    changes = []
    months = []

    for row in csvreader:
    # total number of months included in the dataset
        total_months += 1 
        months.append(row[0])

    # net total amount of "Profit/Losses" over the entire period
        profitlosses = int(row[1])
        total_profitlosses += profitlosses
    
    
    # average of the changes in "Profit/Losses" over the entire period
        profitlosses_change = profitlosses - previous_profitlosses
        changes.append(profitlosses_change)
        previous_profitlosses = profitlosses

    average_change = sum(changes) / (total_months-1)
    
    # greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(changes)
    greatest_increase_index = changes.index(greatest_increase)
    greatest_increase_month = months[greatest_increase_index]
    print(greatest_increase_month)


    #greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(changes)
    greatest_decrease_index = changes.index(greatest_decrease)
    greatest_decrease_month = months[greatest_decrease_index]
    print(greatest_decrease_month)




print("Financial Anaysis")
print("------------------")
print(total_months)
print(total_profitlosses)
print(average_change)
print(changes)
