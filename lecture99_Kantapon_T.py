from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(result)
    if result >= 30:
        lebelResult.configure(text="อ้วนมาก")
    elif result <= 29.9 and result > 24.9:
        lebelResult.configure(text="อ้วน")
    elif result <= 24.9 and result > 22.9:
        lebelResult.configure(text="น้ำหนักเกิน")
    elif result <= 22.9 and result > 18.5:
        lebelResult.configure(text="น้ำหนักปกติ")
    elif result <= 18.5:
        lebelResult.configure(text="ผอมเกินไป")
    

mainWindow = Tk()
labelHeight = Label(mainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text = "น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
lebelResult = Label(mainWindow,text="ผลลัพธ์")
lebelResult.grid(row=2,column=1)
mainWindow.mainloop()