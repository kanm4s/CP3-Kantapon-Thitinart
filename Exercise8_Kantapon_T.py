usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Welcome to KeySoundAddict")
    print("-------------------------")
    print("List of products")

    rubbleKeyboardPrice = 200
    machanicleKeyboardPrice = 2000
    keycapPrice = 1000
    cableUsbCtoAPrice = 100

    print("1. Rubber Keyboard    :",rubbleKeyboardPrice,"THB")
    print("2. Machanicle Keyboard:",machanicleKeyboardPrice,"THB")
    print("3. Keycap             :",keycapPrice,"THB")
    print("4. Cable USBC to A    :",cableUsbCtoAPrice,"THB")
    productInput = int(input("Product Number:"))
    print("How many do you want?")
    productQuantityInput = int(input(">>"))
    if productInput == 1:
        calculate = rubbleKeyboardPrice*productQuantityInput
        print(calculate)
    elif productInput == 2:
        calculate = machanicleKeyboardPrice*productQuantityInput
        print(calculate)
    elif productInput == 3:
        calculate = keycapPrice*productQuantityInput
        print(calculate)
    elif productInput == 4:
        calculate = cableUsbCtoAPrice*productQuantityInput
        print(calculate)