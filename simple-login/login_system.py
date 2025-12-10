print("Simple Login System")
username = "admin"
password = "1234"
tries = 3
for attempt in range(1, tries + 1):
    userattempt = input("Enter Username: ")
    passattempt = input("Enter Password: ")
    if userattempt == username and passattempt == password:
        print("Login Successful")
        break
    elif userattempt != username and passattempt != password:
        print("Both Username and Password are incorrect")
    elif userattempt != username:
        print("Incorrect Username")
    elif passattempt != password:
        print("Incorrect Password")
else:
    print("Tries are Over, Account Locked")
