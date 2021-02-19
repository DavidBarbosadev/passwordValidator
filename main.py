import re
UserInput = input(print("Please introduce your password to verify if it is valid"))
password = UserInput
Detector = 0

while True:
    if len(password) < 8:
        print("Your password is less than 8 Characters")
        Detector = -1
        break
    elif not re.search("[a-z]", password):
        print("Please add some Lower case Characters to your Password")
        Detector = -1
        break
    elif not re.search("[A-Z]", password):
        print("Please add some Upper case Characters to your Password")
        Detector = -1
        break
    elif not re.search("[0-9]", password):
        print("Are you Good ? No Numbers?")
        Detector = -1
        break
    elif not re.search("[_@$]", password):
        print("Dude use special Symbols to make the Password Strong ")
        Detector = -1
        break
    elif re.search('\s', password):
        Detector = -1
        break
    else:
        Detector = 0
        print("Valid Password")
        break

if Detector == -1:
    print("Not a Valid Password")
