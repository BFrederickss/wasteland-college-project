"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Made this file to make the wasteland file cleaner, not sure if this will be a separate file.
            Work mostly done on the functions which will let the player explore the house and gather items and such.



to do:
    - finish all the sublevels of the "Abandoned House" level

"""


from wasteland import *
from world import *

class abandoned_house(world):
    def __init__(self):
        super(abandoned_house,self).__init__()
        self._items = ["Old rusty knife", "Empty bottle", "Old piece of bread", "Old rotten apple"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Abandoned house"
        self._sublocation = "Bedroom"

    def explore_house(self):
        decidelocation = int(input("Where do you want to go? "))
        print("1. Kitchen")
        print("2. Hall")
        print("3. Living room")
        print("4. Basement")
        while True:
            if decidelocation == 1:
                print("Going to the Kitchen")
                self.kitchen()
            elif decidelocation == 2:
                print("Going to the Hall")
                self.hall()
                break
            elif decidelocation == 3:
                print("Going to the Living Room")
                self.living_room()
                break
            elif decidelocation == 4:
                print("Going to the Basement")
                self.basement()
                break
            else:
                print("Wrong answer try again")

    def kitchen(self):
        self._sublocation = "Kitchen"
        self._items = ["Bread", "Bottle of water", "Rusty key", "Map"]

        decide = input("You look around and see the kitchen table, do you want to take a closer look? y/n").lower()
        while True:
            if decide == "y":
                print("You find bread and a bottle of water")
                Player.add_item("Bread")
                Player.add_item("Bottle of water")
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
                Player.add_item("Rusty key")
                Player.add_item("Map")
                break
            elif decide == "n":
                print("You didn't the items from the garbage bin")
                break
            else:
                print("Wrong answer try again")



    def hall(self):
        self._sublocation = "Hall"
        self._items = ["Rotten apple", "Bottle of piss", "Mysterious Fragment"]

        print("You entered the hall and you don't see much, a pool of piss in the corner and some"
                       "rats running around the place. You see three items near that corner. A Rotten apple"
                       ", a Bottle of water and a Mysterious Fragment")

        Player.add_item("Rotten apple")
        Player.add_item("Bottle of piss")
        Player.add_special_item("Mysterious Fragment")

    def living_room(self):
        self._sublocation = "Living Room"
        self._items = []

        print("You entered the Living Room")
        print("You see a mysterious figure near the coffe table")

        # write code for an important NPC

    def basement(self):
        self._sublocation = "Basement"
        self._items = []
        print("You entered the Basement")


