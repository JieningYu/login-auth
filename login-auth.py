import hashlib
import os
import random

def md5(input):
    return hashlib.md5(input.encode()).hexdigest().strip()
def hash_int(input):
    return int(hash(input))

pathT = os.getcwd() + "/data"

if (not os.path.exists(pathT)):
    os.makedirs(pathT)
    user = input("Set your username: ")
    password = input("Set your password: ")
    uf = open(pathT + "/username.txt", "w")

    uf.write(md5(user))
    uf.close()
    pf = open(pathT + "/password.txt", "w")

    pf.write(md5(password))
    pf.close()

success = False
count = 0

while not success:
    user_auth = input("Input your username: ")
    password_auth = input("Input your password: ")
    count += 1

    uf = open(pathT + "/username.txt", "r")
    pf = open(pathT + "/password.txt", "r")

    aa = hash_int(md5(user_auth))
    ab = hash_int(uf.read().strip())

    ba = hash_int(md5(password_auth))
    bb = hash_int(pf.read().strip())

    if aa == ab and ba == bb:
        success = True
        break
    else:
        print("Username of password is wrong!")
    
    if count > random.randint(3, 5):
        print("Tried too many times!")
        break

if success:
    print("Login successfully!")
