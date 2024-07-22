password = 1234
login_count = 0
login_limit = 3
while login_count < login_limit:
    login = int(input("password: "))
    login_count = login_count + 1
    if login == password:
        print("Login Success!")
        break
else:
    print("Login reach limit")