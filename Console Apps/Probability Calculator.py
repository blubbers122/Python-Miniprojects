import tkinter

probArr = [1]
colorCount = {}  # dict with all used colors and amounts

def setUp():
    try:
        total = int(input("Enter number of marbles to draw from: "))
        groups = int(input("Enter total number of unique colors in marble sack (Up to six): "))
    except:
        print("you must enter a positive integer.")

    correct = False
    while not correct:
        left = total
        count = 1
        groupArray = []
        for group in range(groups):
            amt = int(input("Enter # of marbles in group " + str(count) + ": "))
            groupArray.append(amt)
            left = left - amt
            groupsLeft = groups - count
            if left < groupsLeft:
                print("You entered too many marbles in one or more of your groups.\nLet's try again.")
                break
            elif left == groupsLeft == 0:
                print("Done assigning!")
                correct = True
            else:
                if groupsLeft == 0:
                    print("You didn't enter enough marbles in one or more of your groups."
                          "\nLet's try again.")
                else:
                    print("Marbles left to assign: " + str(left))
            if groupsLeft > 0:
                print("Groups left to assign: " + str(groupsLeft))
            count += 1
    prepareCalc(groupArray)

def prepareCalc(groupArray):
    displayMarbles(groupArray)

    print("The marbles were mixed!\n"
          "You can enter your color as many times as you would like "
          "to find the probability of drawing them in that order. Enter 'done' instead of a color when done.")
    choice = ""

    while choice.lower() != "done":
        choice = input("Enter color: ")

        if colorCount[choice.lower()] != 0:
            calcProb(colorCount, choice)
            colorCount[choice.lower()] -= 1
            print(colorCount)
        else:
            print("All of the " + choice.lower() + " marbles were drawn!")
            print(colorCount)


def calcProb(colorCount, choice):
    total = 0
    probability = 1

    for color in colorCount:
        total += colorCount[color]

    probArr.append(colorCount[choice.lower()] / total)

    for prob in probArr:
        probability *= prob

    print(str(total - 1) + " marbles left..")
    print("the probability of drawing your marble(s in succession) is: " + str(round(probability * 100, 6)) + "%")

def displayMarbles(groupArray):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"][:len(groupArray)]

    index = 0
    for color in colors:
        colorCount[color] = groupArray[index]
        print(color + ": " + str(colorCount[color]) + " marbles")
        index += 1

setUp()