"""
MadLibs
Author: Ella J. Wright
Period/Core: 6

"""
print("Madlib: Instructions for petsitter\n")
name = input("Your name: ")
animals = input("Animal (plural): ")
animal1 = input("Name: ")
animal2 = input("Name: ")
verb1 = input("Verb (NOT ending in ing): ")
food = input("Type of food: ")
adjective1 = input("Adjective: ")
room1 = input("Type of room: ")
temperature1 = input("Number: ")
room2 = input("Another type of room: ")
temperature2 = input("Number: ")
noun1 = input("Noun: ")
noun2 = input("Type of liquid: ")
adjective2 = input("Adjective: ")
activity1 = input("Adjective (action): ")
place1 = input("Place: ")

print("\nHello " + name + ",\n"+ "Thank you for agreeing to watch our " + animals + "." + " We wanted to leave you some\ninstructions on what to do/not do for our precious babies.\n")
print("1. Never leave " + animal1 + " and " + animal2 + " alone while they " + verb1)
print(f"2. Always make sure that {animal1} and {animal2}'s {food} is/are {adjective1}")
print(f"3. Make sure that the {room1} is kept exactally at {temperature1}°F, and the\n{room2} is exactally {temperature2}°F")
print(f"\nHere is the schedule to follow each day:")
print("1. Clean the " + noun1)
print(f"2. Empty and refill {animal1}'s and {animal2}'s {noun2}")
print(f"3. Take {animal1}, and {animal2} for a/an {adjective2} {activity1} in the {place1}")
print(f"\nThank you for helping us out!")