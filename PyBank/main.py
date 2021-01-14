import pathlib
import csv

# Collect data from budget_data.csv
budget_data_csv = pathlib.Path('PyBank/Resources/budget_data.csv')

# open and read csv
#with open(budget_data_csv) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")

    #csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

# Define functions are from the parameter budget_data
def financial_analysis(budget_data_csv: list) -> str:

    # assign values to to variales 
    months = str(budget_data_csv[0])
    #profitlosses = (budget_data_csv[1])

    # total number of months included in the data 
    total_months = len(months)

    # The net total amount of "Profit/Losses" over the entire period
    #total_profitlosses = sum(profitlosses)
    
    # average change in profit/losses over the entire period 
    #for date in budget_data_csv:
        #average_change = (sum((profitlosses[2])-1)) / total_months

    # greatest increase in profit (date and amount) over the entire period


    # greatest decrease in losses (date and amount) over the entire period 


    #print(total_months)

    return total_months

assert financial_analysis

print("Financial Anaysis")
print("------------------")
with open(budget_data_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    
    print(financial_analysis(budget_data_csv))
