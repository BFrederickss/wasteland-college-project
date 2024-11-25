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