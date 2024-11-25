"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Just made a separate file for this level, thats all for the time being.

"""

from wasteland import *
from world import *

class old_church(world):
    def __init__(self):
        super(old_church, self).__init__()
        self._items = ["Old cross", "Old bible", "Old candle", "Old chalice"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old church"

    def explore_church(self):
        decidelocation = int(input("Where do you want to go? "))
        print("1. Nave")
        print("2. Crossing")
        print("3. Altar")

        while True:
            if decidelocation == 1:
                print("Going to the Nave")
                break
            elif decidelocation == 2:
                print("Going to the Crossing")
                break
            elif decidelocation == 3:
                print("Going to the Altar")
                break
            else:
                print("Wrong answer try again")