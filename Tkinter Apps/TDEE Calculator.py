from tkinter import *
import tkinter.messagebox
from tkinter import font


def calcTDEE():
    w = weightEntry.get()
    h = heightEntry.get()
    a = ageEntry.get()
    s = sex.get()
    al = default.get()
    met = metVar.get()

    if met == False:
        mResult = str(round((66 + 6.23 * float(w) + 12.7 * float(h) - 6.8 * float(a)) * activityDict[al]))
        fResult = str(round((655 + 4.35 * float(w) + 4.7 * float(h) - 4.7 * float(a)) * activityDict[al]))
    else:
        mResult = str(round((66 + 13.7 * float(w) + 5 * float(h) - 6.8 * float(a)) * activityDict[al]))
        fResult = str(round((655 + 9.6 * float(w) + 1.8 * float(h) - 4.7 * float(a)) * activityDict[al]))

    if s == "female":
        tkinter.messagebox.showinfo("Your TDEE", "Your Total Daily Energy Expenditure was calculated to be " + fResult + " calories.")
    else:
        tkinter.messagebox.showinfo("Your TDEE", "Your Total Daily Energy Expenditure was calculated to be " + mResult + " calories.")


def changeUnits():
    usingMet = metVar.get()
    if usingMet == False:
        weight.config(text="weight in lbs")
        height.config(text="height in inches")
    else:
        weight.config(text="weight in kg")
        height.config(text="height in cm")


activityDict = {  # pairs activity level with BMR multiplier
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Extremely Active": 1.9
}

root = Tk()
root.title("Fitness Calculator")

titlefont = font.Font(family="Helvetica", size=20, weight="bold")
labelfont = font.Font(family="Helvetica", size=14)

container = Frame(root, height=400, width=600).grid(rowspan=9, columnspan=2)
container

title = Label(container, text="TDEE Calculator", font=titlefont, fg="green").grid(row=0, columnspan=2, pady=20)

metVar = BooleanVar()
metric = Checkbutton(container, text="Metric Units?", variable=metVar, command=changeUnits).grid(row=1, columnspan=2)
gender = Label(container, text="gender", font=labelfont).grid(column=0, row=2, rowspan=2, sticky=E, padx=10)
sex = StringVar()
sex.set("male")
maleRadio = Radiobutton(container, text="male", value="male", variable=sex)
maleRadio.grid(row=2, column=1, sticky=W)
femaleRadio = Radiobutton(container, text="female", value="female", variable=sex)
femaleRadio.grid(row=3, column=1, sticky=W)

weight = Label(container, text="weight in lbs", font=labelfont)
weight.grid(row=4, sticky=E, padx=10)
height = Label(container, text="height in inches", font=labelfont)
height.grid(row=5, sticky=E, padx=10)
age = Label(container, text="age in years", font=labelfont).grid(row=6, sticky=E, padx=10)
activityLevel = Label(container, text="activity level", font=labelfont).grid(row=7, sticky=E, padx=10)

weightEntry = Entry()
weightEntry.config(width=22)
weightEntry.grid(row=4, column=1, sticky=W)
heightEntry = Entry()

heightEntry.grid(row=5, column=1, sticky=W)
heightEntry.config(width=22)
ageEntry = Entry()
ageEntry.config(width=22)
ageEntry.grid(row=6, column=1, sticky=W)

default = StringVar()
default.set("Sedentary")
choices = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]

activityDropdown = OptionMenu(container, default, *choices)
activityDropdown.config(width=16)
activityDropdown.grid(row=7, column=1, sticky=W)

submit = Button(container, text="Calculate my TDEE!", bg="green", fg="white", command=calcTDEE).grid(row=8, columnspan=2, pady=30, ipady=10, ipadx=10)

root.mainloop()