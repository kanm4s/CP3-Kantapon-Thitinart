def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("Username or password is incorrect.")
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")


def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatOnly():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    result = (price1+price2) * vat / 100
    return result

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

while login() != True:
    if login() == True:
        break
showMenu()
if menuSelect() == 1:
    print(vatOnly())
else:
    print(priceCalculator())