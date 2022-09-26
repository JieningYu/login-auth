import random

user = input("Set your username: ")
password = input("Set your password: ")

success = False
count = 0

while not success:
    user_auth = input("Input your username: ")
    password_auth = input("Input your password: ")
    count += 1
    if user_auth == user and password_auth == password:
        success = True
        break
    else:
        print("Username of password is wrong!")
    
    if count > random.randint(3, 5):
        print("Tried too many times!")
        break

if success:
    print("Login successfully!")
