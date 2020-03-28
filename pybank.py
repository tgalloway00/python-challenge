import os
import csv

total_months = []
profit_losses = []
average_change = []

# pull data from particular csv
csvpath = os.path.join('budget_data.csv')
with open(csvpath) as budget_data:
    budget_reader = csv.reader(budget_data, delimiter=',')
    # skip over header
    next(budget_reader)

# start for loop to get list of months and list of profits/losses
    for row in budget_reader:
        profit_losses.append(int(row[1]))
        total_months.append(row[0])

# Loop through profit/losses to calculate monthly change
for i in range(len(profit_losses)-1):
    average_change.append(profit_losses[i-1]-profit_losses[i])

# Calculate greatest increase/decrease
max_decrease = min(average_change)
max_increase = max(average_change)

# Associate month with max values
month_decrease = average_change.index(min(average_change)) + 1
month_increase = average_change.index(max(average_change)) + 1

# Define first and last value of the profit/losses column
last_element = (profit_losses[-1])
first_element = (profit_losses[0])
change = (int(last_element) - (int(first_element)))


# Print all values
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(profit_losses)}")
a = ((change) / (len(total_months)))
print(f"Average Change: ${(round(a, 2))}")
print(f"Greatest Increase in Profits: {total_months[month_increase]}  {max_increase}")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]}  {max_decrease}")

# Export text file
output_path = os.path.join("..", "python-challenge", "pybank.csv")

with open(output_path, 'w') as csvfile:
    budget_reader = csv.writer(budget_data, delimiter=',')

    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------"])
    csvwriter.writerow(["Total Months:", len(total_months)])
    csvwriter.writerow(["Total: " , f"${sum(profit_losses)}"])
    csvwriter.writerow(["Average Change:" , f"${round(a, 2)}"])
    csvwriter.writerow(["Greatest Increase in Profits:" , total_months[month_increase] , max_increase])
    csvwriter.writerow(["Greatest Decrease in Profits:" , total_months[month_decrease] , max_decrease])
