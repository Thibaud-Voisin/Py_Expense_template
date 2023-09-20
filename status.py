def show_status():
    expenses = []

    with open('expense_report.csv', mode='r') as file:
        for row in file:
            if(len(row)<5):
                continue
            expense_raw = row.split(',')

            expense = {
                "expense_amount": expense_raw[0],
                "expense_name": expense_raw[1],
                "paid_by": expense_raw[2],
                "debtors": {}
            }

            for i in range(3, len(expense_raw), 2):
                debtor = expense_raw[i]
                amount_owed = float(expense_raw[i + 1])
                expense["debtors"][debtor] = amount_owed

            expenses.append(expense)

    generate_status_report(expenses)


def generate_status_report(expenses):
    tuple_owing = []
    for elt in expenses:
        for key, value in elt["debtors"].items():
            tuple_owing.append((key, value, elt["paid_by"]))
    
    combined_dict = {}

    for a, b, c in tuple_owing:
        if (a, c) in combined_dict:
            combined_dict[(a, c)] += b
        elif (c, a) in combined_dict:
            combined_dict[(c, a)] -= b
        else:
            combined_dict[(a, c)] = b

    combined_list = [(a, b, c) for (a, c), b in combined_dict.items()]

    for i in range(len(combined_list)):
        a,b,c = combined_list[i]
        if b < 0:
            combined_list[i] = (c, abs(b), a)

    print("╭───────────────────────────── Debts ─────────────────────────────╮")
    print("│ {:<12} {:<10} {:<12} {:<2} {:>10} {:<12} │".format("Debtor", "owes", "Creditor", "|", "Amount", "Recipient"))
    print("├─────────────────────────────────────────────────────────────────┤")
    
    for a, b, c in combined_list:
        print("│ {:<12} {:<10} {:<12} │ {:>10.2f} {:<12}  │".format(a, "owes", c, b, "€"))
    
    print("╰─────────────────────────────────────────────────────────────────╯")
