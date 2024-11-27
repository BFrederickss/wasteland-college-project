"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Made this file to make the wasteland file cleaner, not sure if this will be a separate file.
            Work mostly done on the functions which will let the player explore the house and gather items and such.

26/11/2024: Finished the abandoned house level, the player can now explore the house and gather items and clues.



to do:
    - finish all the sublevels of the "Abandoned House" level

"""



from wasteland import Helper1
from wasteland import Player as pl
from world.world import world

class abandoned_house(world):
    def __init__(self):
        super().__init__()
        self.Helper1 = Helper1("Dimitri", "I can help you get through this level")
        self._items = ["Old rusty knife", "Empty bottle", "Old piece of bread", "Old rotten apple"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Abandoned house"
        self._sublocation = "Bedroom"
        self.pl = pl("John")

    def explore_house(self):
        print("1. Kitchen")
        print("2. Hall")
        print("3. Living room")
        print("4. Basement")
        print("5. Check menu")
        decidelocation = int(input("Where do you want to go? "))

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
            elif decidelocation == 5:
                break
            else:
                print("Wrong answer try again")
                print("1. Kitchen")
                print("2. Hall")
                print("3. Living room")
                print("4. Basement")
                print("5. Check inventory")
                print("6. Check clues")
                print("7. Exit the house")
                decidelocation = int(input("Where do you want to go? "))

        return None

    def kitchen(self):
        self._sublocation = "Kitchen"
        self._items = ["Bread", "Bottle of water", "Rusty key", "Map"]

        decide = input("You look around and see the kitchen table, do you want to take a closer look? y/n").lower()
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





    def hall(self):
        self._sublocation = "Hall"
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



    def living_room(self):
        self._sublocation = "Living Room"
        self._items = []


        print("You entered the Living Room")
        print("You see a mysterious figure near the coffe table")

        self.Helper1.tutorial()
        self.Helper1.provide_clue("You should go to the old church, there might be something there that will help you",
                                  "Go to the old church, find gold Belarusian coin",
                                  "If you want another clue, comeback with a golden Belarusian coin. you can go away now...")

        self.explore_house()



    def basement(self):
        self._sublocation = "Basement"
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


