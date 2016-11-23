# File: hw6.py
# Author: Uzoma Uwanamodo
# Date: 10/21/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A simple math helper program
# Collaboration:
# I did not collaborate with anyone on this assignment


# printOneHouse() Print the list of students in the specified house
# Input: registry, the dictionary that contains the houses registries; house, the name of the house
# Output: houseRoll, the list of the students within the house
def printOneHouse(registry, house):
    
    # Check to see if the house exists and retrieve the registry if it does
    if house in registry:
        houseRoll = registry.house
    else:
        houseRoll = []
    
    return houseRoll


def main():
    
    print(printOneHouse(registry, house))
    
main()