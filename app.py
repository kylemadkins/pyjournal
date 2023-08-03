import datetime

from models.entry import Entry
from db import init_db

init_db()

welcome = "Welcome to the programming journal!"
menu = """\nPlease select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: """

print(welcome)

option = input(menu)
while option != "3":
    if option == "1":
        content = input("\nTell me what you did today:\n")
        entry = Entry.create(datetime.date.today(), content)

    elif option == "2":
        for entry in Entry.all():
            print(entry)

    else:
        print("\nInvalid option\n")

    option = input(menu)
