BEGIN
    PROMPT user to enter the budgeted amount
    SET total_expenses to 0

    WHILE user has more expenses
        PROMPT user to enter an expense
        ADD expense to total_expenses

    IF total_expenses > budgeted_amount
        PRINT "You are over budget by" (total_expenses - budgeted_amount)
    ELSE
        PRINT "You are under budget by" (budgeted_amount - total_expenses)
END
