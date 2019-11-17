# Jewel Newman
# CSCI 102 - Section B
# Week 12 - Part A

def PrintOutput(statement):
    print("OUTPUT", statement)

# PrintOutput("Hello World")

def LoadFile(filename):
    file = open(filename)
    return file.readlines()
