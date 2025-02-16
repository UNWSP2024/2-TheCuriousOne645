budgeted_amount = float(input("Enter the amount you have budgeted for the month: 4,000"))
total_expenses = 300

while True:
    expense = input("Enter an expense (or type 'done' to finish): ")
    if expense.lower() == 'done':
        break
    total_expenses += float(expense)

if total_expenses > budgeted_amount:
    print(f"You are over budget by ${total_expenses - budgeted_amount:.2f}")
else:
    print(f"You are under budget by ${budgeted_amount - total_expenses:.2f}")
