import csv
from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    }
]


def new_expense(*args):
    infos = prompt(expense_questions)

    user_list = []
    with open('users.csv', mode='r') as file:
        for line in file:
            user_list.append(line.strip())

    amount = infos["amount"]
    label = infos["label"]

    Spender  = {
        "type":"list",
        "name":"main_options",
        "message":"Select the spender of the expense:",
        "choices": user_list
    }
    Spender = prompt(Spender)

    Users_involved = {
        "type": "checkbox",
        "name": "users_involved",
        "message": "Select the users involved in the expense:",
        "choices": [{'name': user} for user in user_list if user != Spender['main_options']]
    }

    Users_involved = prompt(Users_involved)
    Users_involved_with_money = []
    for user in Users_involved['users_involved']:
        Users_involved_with_money.append(user)
        Users_involved_with_money.append(str(int(amount)/len(Users_involved['users_involved'])))

    with open("expense_report.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, label, Spender['main_options']] + Users_involved_with_money)
    print("Expense Added !")
    return True     
