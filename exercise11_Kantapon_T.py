numberInput = int(input("Enter number: "))
numberSpace = 0
for i in range(numberInput):
    space = " "
    text = "*"
    for x in range(i):
        text += "*"+"*"
    numberSpace = numberInput-(i+1)
    space = space*(numberSpace)
    print(space+text)
        