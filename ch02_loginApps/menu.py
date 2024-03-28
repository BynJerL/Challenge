import accountBank as acc
from time import sleep

def help_menu():
    print(f"List of commands:\n\th\t: help.\n\tq\t: quit.\n\tlogin\t: log-in.\n\ts\t: start")

def login():
    username = str(input("Username: "))
    password = str(input("Password: "))

    for i in range(0, len(acc.accountList)):
        if acc.accountList[i]['username'] == username:
            if acc.accountList[i]['password'] == password:
                print(f"Access granted. Welcome, {username}!")
                return

    print("Invalid username or password\n")       

def start():
    print("START")

    for i in range(0, 5):
        sleep(1)
        print('.')
    
    sleep(1)
    print()

while True:
    myInput = str(input("Input anything, press h for help: "))

    if myInput in ['h', 'help']:
        help_menu()
    elif myInput in ['q', 'quit', 'exit', 'ext']:
        break
    elif myInput in ['s', 'start']:
        start()
    elif myInput in ['login']:
        login()
    else:
        continue

