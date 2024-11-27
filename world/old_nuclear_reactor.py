"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Just made a separate file for this level, thats all for the time being.

"""

from wasteland import *
from world import *

class old_nuclear_reactor(world):
    def __init__(self):
        super(old_nuclear_reactor, self).__init__()
        self._items = ["Old uranium rod", "Old nuclear reactor manual", "Old nuclear reactor key", "Old nuclear reactor button"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old nuclear reactor"

    def explore_reactor(self):
        decidelocation = int(input("Where do you want to go? "))
        print("1. Containment building")
        print("2. Control room")
        print("3. Auxiliary room")
        print("4. Diesel generator")
        while True:
            if decidelocation == 1:
                print("Going to the Containment building")
                break
            elif decidelocation == 2:
                print("Going to the Control room")
                break
            elif decidelocation == 3:
                print("Going to the Auxiliary room")
                break
            elif decidelocation == 4:
                print("Going to the Diesel generator")
                break
            else:
                print("Wrong answer try again")


# portal will be here