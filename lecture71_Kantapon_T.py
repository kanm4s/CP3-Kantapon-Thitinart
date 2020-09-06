menuList = []
priceList = []

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        priceList.append(int(input("Price :")))
        menuList.append(menuName)

def showBill():
    print("----- My Food -----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += priceList[number]
    print("total", totalPrice,"THB")

showBill()