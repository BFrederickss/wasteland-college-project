"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: Just made a separate file for this level, thats all for the time being.

"""

from wasteland import *
from world import *

class old_rotten_school(world):
    def __init__(self):
        super(old_rotten_school, self).__init__()
        self._items = ["Old rusty scissors", "Old chalk", "Old ruler", "Old pen"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old rotten school"

    def explore_school(self):
        decidelocation = int(input("Where do you want to go? "))
        print("1. Classroom")
        print("2. Secretary office")
        print("3. Principal office")
        print("4. Library")
        while True:
            if decidelocation == 1:
                print("Going to the Classroom")
                break
            elif decidelocation == 2:
                print("Going to the Secretary Office")
                break
            elif decidelocation == 3:
                print("Going to the Principal Office")
                break
            elif decidelocation == 4:
                print("Going to the Library")
                break
            else:
                print("Wrong answer try again")