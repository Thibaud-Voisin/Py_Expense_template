import csv
from PyInquirer import prompt

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "Please enter your name: ",
    }
]

def add_user(*args):
    user_data = prompt(user_questions)

    user_name = user_data["name"]
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_name])
    print("User Added !")
    return True