from hash import hash_sha3_256 as key_encrypt
from accountData import registeredAccount as accounts

"""
key_in = input("Enter keyword: ")
result = key_encrypt(key_in)
if result == keyword:
    print("Access granted")
else:
    print("Access denied")
"""
try:
    email = input("Email address: ")

    for account in accounts:
        if account['user_email'] == email:
            chance = 3

            while(chance > 0):
                password = input("Your password: ")

                if account['password'] == key_encrypt(password):
                    print("Access granted")
                    exit()
                else:
                    print("Incorrect password")
                    chance -= 1
            print("Access denied")
            exit()

    print("Account not found")
    
except KeyboardInterrupt:
    print("\nYou have pressed ctrl+c button. Force closing the program")