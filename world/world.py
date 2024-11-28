"""
THIS IS A TEMP FILE, NOT SURE IF IT WILL BE SEPARATE

Author: Konrad Malara

Date started: 25/11/2024

description: world class that will show the player where they are and where they can go
             the player will have to find clues to get to the next level
             the player will have to find food and water to survive
             the player will have to find items to help them get through the level

Updates:
25/11/2024: Just made a separate file for this level, thats all for the time being.

"""


class world:
    def __init__(self):
        self._levels = ["Old church", "Abandoned house", "Quiet farm", "Old nuclear reactor", "Old rotten school"]
        self._player_location = "Abandoned house"

    def view_world(self):
        print("You are currently in: ", self._player_location)
        for i in self._world:
            print(i)

# locations in the world
# each location will have items and clues that the player can find
# 25/11/2024 17:32: Decided to move the locations to their own respective files
