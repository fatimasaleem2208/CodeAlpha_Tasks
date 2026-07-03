correct_username = "admin"
correct_password = "StrongPass123"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Invalid username or password.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked. Too many failed login attempts.")
