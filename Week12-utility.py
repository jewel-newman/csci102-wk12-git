# Jewel Newman
# CSCI 102 - Section B
# Week 12 - Part A

def PrintOutput(statement):
    print("OUTPUT", statement)

def LoadFile(filename):
    file = open(filename)
    return file.readlines()

def UpdateString (string1, string2, indexnum):
    editedString = ""
    for index, char in enumerate(string1):
        if index == indexnum:
            editedString += string2
        else:
            editedString += char
    print("OUTPUT", editedString)

def FindWordCount(loadList, foundString):
    counter = 0
    for word in loadList:
        if word == foundString:
            counter += 1
    return counter

def ScoreFinder(playerNames, playerScores, nameWanted):
    score = 0
    check = 0
    playerName = ""
    nameWanted = nameWanted.lower()
    for index, name in enumerate(playerNames):
        if nameWanted == name.lower():
            score = playerScores[index]
            check += 1
            playerName = playerNames[index]
    if check == 1:
        print("OUTPUT", playerName, "got a score of", score)
    else:
        print ("OUTPUT player not found")

def Union(list1, list2):
    combinedList = list1 + list2
    return list(dict.fromkeys(combinedList))

def Intersection(list1, list2):
    finalList = []
    for thing1 in list1:
        for thing2 in list2:
            if thing2 == thing1:
                finalList.append(thing1)
    return finalList

def NotIn(list1, list2):
    finalList = []
    check = 0
    for thing1 in list1:
        for thing2 in list2:
            if thing1 == thing2:
                check += 1
        if check == 0:
            finalList.append(thing1)
            check = 0
    return finalList

