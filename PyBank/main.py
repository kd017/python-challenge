import csv
import os

# Create input path; Assumes the program is executed from PyBank directory
input_path = os.path.join('Resources', 'budget_data.csv')

# Open the file
with open(input_path, 'r') as input_file:

    # Create a CSV reder
    csvreader = csv.reader(input_file)

    # Skip the Header
    header = next(csvreader)

    # Holders to keep track of num months and total
    num_months = 0
    total_change = 0
    prev_month_pl = 0

    # Holders to keep track of greatest increase
    greatest_increase_month = None
    greatest_increase = 0

    # Holders to keep track of greatest decrease
    greatest_decrease_month = None
    greatest_decrease = 0

    # Iterate through Rows
    for row in csvreader:
        month = row[0]
        profit_loss = float(row[1])

        # Add current month's P/L to total
        num_months += 1

        # monthly change
        change = profit_loss - prev_month_pl
        prev_month_pl = profit_loss
        total_change += change

        # Check if current month's P/L is more than current max
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = month

        # Check if current month's P/L is less than current min
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = month
    
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: ${total_change}')
print(f'Average  Change: ${total_change/num_months:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

with open('results.txt', 'w') as output_file:
    output_file.write('Financial Analysis\n')
    output_file.write('----------------------------\n')
    output_file.write(f'Total Months: {num_months}\n')
    output_file.write(f'Total: ${total_change}\n')
    output_file.write(f'Average  Change: ${total_change/num_months:.2f}\n')
    output_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    output_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')



