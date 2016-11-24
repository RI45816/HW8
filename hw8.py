# File: hw6.py
# Author: Uzoma Uwanamodo
# Date: 10/21/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A simple math helper program
# Collaboration:
# I did not collaborate with anyone on this assignment


import random


MENU_OPTIONS = ["Print a single house","Print all the houses","Sort a new person into a house","Exit the program"]
EXIT_NUMBER = 4



# printOneHouse() Print the list of students in the specified house
# Input: registry, the dictionary that contains the houses registries; house, the name of the house
# Output: None
def printOneHouse(registry, house):
    
    # Check to see if the house exists and retrieve the registry if it does
    if house in registry:
        print("The members of the House of %s are:\n\t%s" % (house, "\n\t".join(registry[house])))
    else:
        print("There is no house by the name of",house)
    
    return

# printAllHouses() Print a list of the students by house
# Input: registry, the dictionary that contains the houses registries
# Output: None
def printAllHouses(registry):
    
    # Run printOneHouse() on every house in the registry
    for house in registry:
        printOneHouse(registry, house)
    return

# readRegistryFile() Read a file and add the students to the registry
# Input: registry, the dictionary that contains the houses registries; fileName, the name of the file
# Output: registry, an updated registry
def readRegistryFile(registry,fileName):
    registryFile = open(fileName)
    
    # For every line in the file, parse the entries and put them into the dictionary
    for i in list(registryFile):
        entry = i.split(",")
        if entry[0].strip() in registry:
            registry[entry[0].strip()].append(entry[1].strip())
        else:
            registry[entry[0].strip()] = []
            registry[entry[0].strip()].append(entry[1].strip())
            
    return registry
    
    
# houseSort() Sort the user into a house at random, while taking preference into account
# Input: registry, the dictionary that contains the houses registries; person, the name of the person who is to be sorted; preference, the house the person would prefer to be sorted into
# Output: registry, the updated dictionary with the newly sorted person inside
def houseSort(registry, person, preference):
    
    # Get a list of current houses
    houses = list(registry.keys())
    
    # If the user prefers one of the available houses, take that into consideration, otherwise, ignore their preference (or lack thereof) and sort the user
    if preference in houses:
        # Get the array index number of the preffered choice
        preferenceIndex = houses.index(preference)
        
        # Generate an array as long as the list of houses, filled with the index number of the preffered house and concatenate an array of the indexes of all the houses, and choice a random number from that array and use it as the index to get a random house
        house = houses[random.choice([preferenceIndex] * len(houses) + list(range(len(houses))))]
    else:
        # Take an array of all the indexes of all the houses and pick randomly from that list
        house = houses[random.randrange(len(houses))]
    
    # add the sorted user to the dictionary
    registry[house].append(person)
    
    print(person, "was sorted into house", house)
    return registry
        
    
def main():
    
    # Load the registry
    registry = {}
    registry = readRegistryFile(registry, input("Please enter filename to load from: "))
#    registry = readRegistryFile(registry, "GoT.txt")
#    registry = readRegistryFile(registry, "HP.txt")
#    registry = readRegistryFile(registry, "short_HP.txt")

    # Prompt user for file with dictionary entries
#    fileName = input("Please enter filename to load from: ")
#    registry = readRegistryFile(registry, fileName)
#    registry = houseSort(registry, "Uzoma Uwanamodo", "Gryff")
    
    
    # Print menu options
    print("\nPlease make a choice from the menu:\n%s\n" % "\n".join(["%s - %s" % (i+1, MENU_OPTIONS[i]) for i in range(len(MENU_OPTIONS))]))

    # Request user to make a choice
    choice = input("Please enter a number between 1 and 4 (inclusive): ")
    
    # While the user chooses not to quit
    while choice != str(EXIT_NUMBER):
        
        if choice not in [str(i+1) for i in range(len(MENU_OPTIONS)-1)]:
            print("I'm sorry, that's not an option")
        else:
            choice = int(choice)
            # User chooses to print a single house
            if choice == 1:
                
                # Ask user for which house, and print it
                printOneHouse(registry, input("What house's members would you like to print? "))
            
            # User chooses to print all the houses
            elif choice == 2:
                printAllHouses(registry)
            
            # User chooses to sort a person into one of the houses
            elif choice == 3:
                
                # Ask for the person's name and preffered house, then sort
                houseSort(registry, input("What is the person's name? "), input("What house do they prefer? "))
                
        print("\n----- ----- ----- ----- ----- -----")
        
        # Print menu options
        print("\nPlease make a choice from the menu:\n%s\n" % "\n".join(["%s - %s" % (i+1, MENU_OPTIONS[i]) for i in range(len(MENU_OPTIONS))]))
        
        # Request user to make a choice
        choice = input("Please enter a number between 1 and 4 (inclusive): ")
        
    # Thank the user and close the program
    print("Thank you for using the Great Houses Program")

main()