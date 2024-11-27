"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Just made a separate file for this level, thats all for the time being.

"""

from wasteland import *
from world import *

class quiet_farm(world):
    def __init__(self):
        super(quiet_farm, self).__init__()
        self._items = ["Old rusty pitchfork", "Old hoe", "Old shovel", "Old rake"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Quiet farm"

    def explore_farm(self):
        decidelocation = int(input("Where do you want to go? "))
        print("1. Barn")
        print("2. Radioactive wheat field")
        print("3. Grave")
        print("4. Stable")
        while True:
            if decidelocation == 1:
                print("Going to the Barn")
                break
            elif decidelocation == 2:
                print("Going to the Radioactive Wheat Field")
                break
            elif decidelocation == 3:
                print("Going to the Grave")
                break
            elif decidelocation == 4:
                print("Going to the Stable")
                break
            else:
                print("Wrong answer try again")


    def barn(self):
        self._sublocation = "Barn"
        self._items = ["Bread", "Bottle of vodka", "Belarusian gold coin"]

        decide = input("You look around and see the big stack of wheat, do you want to take a closer look? y/n").lower()
        while True:
            if decide == "y":
                print("You find bread and a bottle of water")
                self.pl.add_item('Bread')
                self.pl.add_item("Bottle of water")
                break
            elif decide == "n":
                print("You didn't get closer to the table")
                break
            else:
                print("Wrong answer try again")

        decide = input("You see a garbage bin at the corner, do you want to check it out? y/n").lower()
        while True:
            if decide == "y":
                print("You find a Rusty key and a Map on the floor")
                self.pl.add_item("Rusty key")
                self.pl.add_item("Map")
                break
            elif decide == "n":
                print("You didn't the items from the garbage bin")
                break
            else:
                print("Wrong answer try again")

        decide = input("Do you still want to explore the kitchen? y/n").lower()
        while True:
            if decide == 'y':
                continue
            else:
                self.explore_house()





    def field(self):
        self._sublocation = "Radioactive wheat field"
        self._items = ["Rotten apple", "Bottle of piss", "Mysterious Fragment"]

        print("You entered the hall and you don't see much, a pool of piss in the corner and some"
                       "rats running around the place. You see three items near that corner. A Rotten apple"
                       ", a Bottle of water and a Mysterious Fragment")

        self.pl.add_item("Rotten apple")
        self.pl.add_item("Bottle of piss")
        self.pl.add_special_item("Mysterious Fragment")

        print("There's a door at the end of the hall, do you want to open it? y/n")
        decide = input().lower()
        while True:
            if decide == 'y':
                print("You tried to open the door, its locked...")
                break
            elif decide == 'n':
                print("You decided to leave the door alone")
                break
            else:
                print("Wrong answer try again")

        print("Theres nothing much in the hall, you decide to move on")
        self.explore_house()



    def grave(self):
        self._sublocation = "Grave"
        self._items = []


        print("You entered the Living Room")
        print("You see a mysterious figure near the coffe table")

        self.Helper1.tutorial()
        self.Helper1.provide_clue()

        self.explore_house()



    def stable(self):
        self._sublocation = "Stable"
        self._items = []
        print("You entered the Basement")


        print("You find a secret door in the basement, do you want to open it? y/n")
        decide = input().lower()
        while True:
            if decide == 'y':
                print("You're out of the house, you can now decide where you want to go")
                break
            elif decide == 'n':
                print("You decide to leave the basement")
                break
            else:
                print("Wrong answer try again")

        return None