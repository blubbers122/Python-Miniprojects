class Character:
    def __init__(self, name, hp, strength, speed, id):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.id = id


charDict = {
    "Bob": Character("Bob", 10, 4, 5, 1),
    "Tom": Character("Tom", 13, 3, 4, 2)
}


attackArr = [["punch", "punches", 2], ["kick", "kicks", 1], ["scratch", "scratches", 1]]


def printCharStats():
    ind = 1
    for char in charDict:
        x = charDict[char]
        print("{}. {} has {} hp, {} strength, and {} speed.".format(ind, x.name, x.hp, x.strength, x.speed))
        ind += 1


def printFightOptions():
    for attack in attackArr:
        ind = attackArr.index(attack)
        print("{}. {}".format(ind + 1, attackArr[ind][0]))


def battle(myChar, oppChar):
    stillFighting = True
    if myChar.speed >= oppChar.speed:
        turn = 0
        currentChar = myChar
        otherChar = oppChar
    else:
        turn = 1
        currentChar = oppChar
        otherChar = myChar
    while stillFighting:
        print(currentChar.name + "'s turn...")
        printFightOptions()
        attChoice = input("choose your attack:\n")

        attack = attackArr[int(attChoice) - 1][1]
        rawDamage = currentChar.strength * attackArr[int(attChoice) - 1][2]

        remainingHp = otherChar.hp - rawDamage
        otherChar.hp = remainingHp
        print("{} {} {}!".format(currentChar.name, attack, otherChar.name))
        if remainingHp <= 0:
            print("{} fainted!\n{} wins!".format(otherChar.name, currentChar.name))
            stillFighting = False
        else:
            print("{} took {} damage and has {}hp left.\n".format(otherChar.name, rawDamage, remainingHp))
        turn += 1
        if turn % 2 == 0:
            currentChar = myChar
            otherChar = oppChar
        else:
            currentChar = oppChar
            otherChar = myChar


def preBattle():
    printCharStats()
    charChoice = input("Choose your character:\n")
    for char in charDict:
        x = charDict[char]
        if int(charChoice) == x.id:
            myChar = x

    print("You chose " + myChar.name + "\n")
    printCharStats()
    oppChoice = input("Choose your opponent:\n")
    for char in charDict:
        x = charDict[char]
        if int(oppChoice) == x.id:
            oppChar = x

    print("{} vs. {}".format(myChar.name, oppChar.name))
    print("FIGHT!\n")
    battle(myChar, oppChar)


def createChar(newCharId):
    print("Create your character:")
    name = input("Enter name\n")
    hp = input("Enter hp\n")
    strength = input("Enter strength\n")
    speed = input("Enter speed\n")
    charDict[name] = Character(name, int(hp), int(strength), int(speed), newCharId)
    char = charDict[name]
    reviewStr = "{} has {} hp, {} strength, and {} speed. They have been added to the roster.\n"
    print(reviewStr.format(char.name, char.hp, char.strength, char.speed))


def mainMenu():
    newCharId = 3
    inMenuLoop = True
    while inMenuLoop:
        Menuchoice = input("1. fight with set characters\n2. create custom character?\n3. exit\n")
        if Menuchoice == "1":
            preBattle()
        if Menuchoice == "2":
            createChar(newCharId)
            newCharId += 1
        else:
            break

mainMenu()
