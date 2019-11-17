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

