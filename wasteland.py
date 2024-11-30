"""
file for the wasteland level

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: This file was created as the base of the game is needed to be done. The game will be a text based adventure
            game that will have a few levels. The player will have to survive in the wasteland and find clues to get to the
            next level. The game will have a few(or maybe just 1) NPCs that will help the player get through the level.
            The player will have to find food and water to survive.

26/11/2024: Finally decided to check if my files even work and run, they do. Finished abandoned_house file, wasteland file
            had its own issues with the player class, such as player add item but that was fixed. Made it so the player
            can explore the house and get items and clues. Made it so the player can check their inventory and status.
            The player can also go back to menu and quit the game. The game is somewhat playable now with only one level.

to do:

- make the game somewhat playable
- make the wolrd class workable



"""

from threading import Thread
import time



# game class that will run the game
# its here for now, as of 25th November, will not do a lot of things to it
# right now, but will add more to it as the game progresses.
class Characters:
    def __init__(self,name, dialogue):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False


    def interaction(self):
        if not self._interacted:
            interaction = f"{self._name}: f{self._dialogue}"
        else:
            interaction = f"{self._name}: no longer interested in talking to you"

        return interaction

# more important characters
# they will help the player get through the level
class Helper1(Characters):
    def __init__(self, name, dialogue):
        super(Helper1, self).__init__(name, dialogue)
        self._name = "dimitri"
        self.pl = Player("John")

    # def __repr__(self):
    #     return f"{self._name} {self._dialogue}"

    def provide_clue(self, clue, quest, narrative):
        print(clue)
        self.pl.add_clue(clue)
        self.pl.add_quest(quest)
        print(narrative)




class Player:
    def __init__(self, name):
        self.hungerBar = 10
        self.thirstBar = 10
        self.healthBar = 10
        self._name = name
        self.space = []
        self.specialspace = []
        self.__clues = []
        self.quest = []
        self._location = "Abandoned house"
        self.__food = ["Bread", "Pure apple", "Ribs"]
        self.__toxic_food = ["Rotten apple", "Rotten meat", "Rotten bread"]
        self.__liquid = ["Bottle of water", "Bottle of vodka", "Bottle of beer"]
        self.__toxic_liquid = ["Bottle of poison", "Bottle of acid", "Bottle of bleach"]

    # Inventory mechanic, not final
    def check_if_full(self):
        if len(self.space) == 10:
            print("You're invetory is full")

    # Views the inventory
    def view_invetory(self):
        if len(self.space) == 0:
            print("You have no items in your inventory")
        else:
            for i in range(len(self.space)):
                print(self.space[i])

    # Hunger bar and thirst bar decay over time so the player is forced
    # to explore the world a lot more and to find food/water for survival
    def __clock_tick(self):
        self.hungerBar -= 1
        self.thirstBar -= 1



        self.death()

    # Calls back clock tick so the hunger bar and thirst bar can get low
    # over time
    def call_clock_tick(self):
        while True:
            time.sleep(20)
            self.__clock_tick()




    # I dont think this is final
    # death mechanic needs to be worked on
    def death(self):
        while True:
            if self.hungerBar == 0:
                self.healthBar =-2

            if self.thirstBar == 0:
                self.healthBar =-1

            if self.healthBar == 0:
                print("You have died")
                return True

    #
    def add_item(self, item):
        self.check_if_full()
        ans = input(f"Would you like to add {item} to the inventory? y/n: ")

        while True:
            if ans == 'y':
                self.space.append(item)
                break
            elif ans == 'n':
                print("Item discarded")
                break
            else:
                print("Wrong answer try again")
                ans = input(f"Would you like to add {item} to the inventory? y/n: ")

    def add_special_item(self, item):
        ans = input(f"Would you like to add {item} to the inventory? y/n: ")

        while ans == 'y' or ans == 'n':
            if ans == 'y':
                self.specialspace.append(item)
                break
            elif ans == 'n':
                print("Item discarded")
                break
            else:
                print("Wrong answer try again")

    def use_item(self):
        print("What do you want to eat?")
        for i in self.space:
            print(i + 1, self.space[i])

        decide = int(input())

        if self.space[decide] in self.__food:
            if self.hungerBar == 8:
                self.hungerBar += 2
                print(f"You have eaten {self.space[decide]}")
            else:
                print("You are not hungry")

        if self.space[decide] in self.__toxic_food:
            self.healthBar -= 2
            print(f"You have eaten {self.space[decide]}")

        if self.space[decide] in self.__liquid:
            if self.thirstBar == 8:
                self.thirstBar += 2
                print(f"You have drank {self.space[decide]}")
            else:
                print("You are not thirsty")

        if self.space[decide] in self.__toxic_liquid:
            self.healthBar -= 2
            print(f"You have drank {self.space[decide]}")


    def review_clues(self):
        if len(self.__clues) > 0:
            for i in self.__clues:
                print(i)
        else:
            print("You have no clues yet")

    def add_clue(self,clue):
        self.__clues.append(clue)

    def add_quest(self, quest):
        self.quest.append(quest)

    def view_quest(self):
        for i in self.quest:
            print(i)


class Level1:
    def __init__(self):
        self.pl = Player("John")
        self._wd = world()
        self._ah = abandoned_house(self.pl)
        self._nr = old_nuclear_reactor(self.pl)
        self._helpers = [Helper1("Xavier", "I can help you get through this level")]
        self._qf = quiet_farm(self.pl)
        self.levels = self._wd._levels
        self.completed = False




    def start(self):
        print("Welcome to the wasteland"
              "You have been teleported to this land by a mysterious force")
        print("You have to survive in this land by finding food and water")
        print("You also have to find clues to get to the next level")
        print("Good luck")
        print("")

        while True:

            if self._nr.finished:
                self.completed = True
                return None

            print("What do you want to do?")
            for i in range(len(self.pl.space)):
                if self.pl.space[i] == "Map":
                    print("1. look at the map")
                    break
            else:
                print("1. explore the house")


            print("2. Check your status")
            print("3. Check inventory")
            print("4. Quit")
            print("")

            choice = input("Enter your choice: ")

            if choice == "1":
                if self.pl.hungerBar < 5:
                    print("You feel hungry")
                if self.pl.thirstBar < 5:
                    print("You feel thirsty")
                print("")

                for i in range(len(self.pl.space)):
                    if self.pl.space[i] == "Map":
                        print("Where do you want to go?")
                        print("1. Abandoned house")
                        print("2. Quiet farm")
                        print("3. Old nuclear reactor")

                        decide = int(input())
                        while True:
                            if decide == 1:
                                print("Going to the abandoned house")

                                self._ah.explore_house()
                                break
                            elif decide == 2:
                                print("Going to the quiet farm")
                                self._qf.explore_farm()
                                break
                            elif decide == 3:
                                print("Going to the old nuclear reactor")
                                self._nr.explore_reactor()
                                break
                            else:
                                print("Invalid choice")
                                print("Where do you want to go?")
                                decide = int(input())

                        break
                else:
                    print("Exploring the house...")
                    self._ah.explore_house()




            elif choice == "2":
                print(f"Your hunger: {self.pl.hungerBar}")
                print(f"Your thirst: {self.pl.thirstBar}")
                print(f"Your health: {self.pl.healthBar}")
                print("")

            elif choice == "3":
                if len(self.pl.space) == 0:
                    print("You have no items")
                    print("")
                    continue
                else:
                    print("You have the following items:")

                    for i in range(len(self.pl.space)):
                        print(self.pl.space[i])

                    decide = input("Would you like to eat or drink something? y/n: ").lower()
                    if decide == 'y':
                        self.pl.use_item()
                    elif decide == 'n':
                        print("You decided not to eat or drink anything")
                    else:
                        print("Wrong answer try again")
                        decide = input("Would you like to eat or drink something? y/n: ").lower()

            elif choice == "4":
                print("Goodbye")
                break

            else:
                print("Invalid choice")
                print("")






class world:
    def __init__(self):
        self._levels = ["Old church", "Abandoned house", "Quiet farm", "Old nuclear reactor", "Old rotten school"]
        self._player_location = "Abandoned house"

    def view_world(self):
        print("You are currently in: ", self._player_location)
        for i in self._world:
            print(i)


class abandoned_house(world):
    def __init__(self, Player):
        super().__init__()
        self.Helper1 = Helper1("Dimitri", "I can help you get through this level")
        self.pl = Player

    def explore_house(self):
        background_thread = Thread(target=self.pl.call_clock_tick)
        background_thread.start()

        while True:
            print("1. Kitchen")
            print("2. Hall")
            print("3. Living room")
            print("4. Basement")
            print("5. Check menu")
            decidelocation = int(input("Where do you want to go? "))


            if decidelocation == 1:
                print("Going to the Kitchen")
                self.kitchen()

            elif decidelocation == 2:
                print("Going to the Hall")
                self.hall()

            elif decidelocation == 3:
                print("Going to the Living Room")
                self.living_room()

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
                print("5. Check menu")
                decidelocation = int(input("Where do you want to go? "))

        return None


    def kitchen(self):
        decide = input("You look around and see the kitchen table, do you want to take a closer look? y/n").lower()


        print("You found a Rusty key and a Map on the floor")
        self.pl.add_item("Rusty key")
        self.pl.add_item("Map")

        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        print("You decide to leave the kitchen")

        #return None


    def hall(self):


        print("You entered the hall and you don't see much, a pool of dirty water in the corner and some"
                       "rats running around the place. You see 2 items near that corner. A Rotten apple"
                       " and a Mysterious Fragment")

        self.pl.add_item("Rotten apple")
        self.pl.add_item("Bottle of water")
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
        #return None



    def living_room(self):
        print("You entered the Living Room")
        print("You see a mysterious figure near the coffe table")

        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("Hello wanderer, my name is Dimitri, I am here to help you get through the wasteland")
        time.sleep(3)
        print("This land is accursed with radiation and undead creatures, you must be careful")
        time.sleep(3)
        print("I can give you some hints and clues to help you get through this level")
        time.sleep(3)
        print("You have to find food and water to survive in this land")
        time.sleep(3)
        print("You also have to find clues to get to the next level")
        time.sleep(3)
        print("I can give you a clue to help you get through this level")
        self.Helper1.provide_clue("You should go to the quiet farm, there might be something there that will help you",
                                  "Go to the old church, find gold Belarusian coin",
                                  "If you want to get out of here, comeback with a golden Belarusian coin. you can go away now...")

        #return None



    def basement(self):
        print("You entered the Basement")
        print("You find a secret door in the basement, do you want to open it? y/n")
        decide = input().lower()
        while True:
            if decide == 'y':
                print("You're out of the house, you can now decide where you want to go")
                break

            elif decide == 'n':
                print("You decide to leave the basement")
                self.explore_house()
            else:
                print("Wrong answer try again")
                decide = input().lower()

        #return None


class quiet_farm(world):
    def __init__(self, Player):
        super().__init__()
        self._items = ["Old rusty pitchfork", "Old hoe", "Old shovel", "Old rake"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Quiet farm"
        self.pl = Player
        self.healthBar = self.pl.healthBar

    def explore_farm(self):
        while True:
            print("1. Barn")
            print("2. Radioactive wheat field")
            print("3. Check menu")

            decidelocation = int(input("Where do you want to go? "))

            if decidelocation == 1:
                print("Going to the Barn")
                self.barn()

            elif decidelocation == 2:
                print("Going to the Radioactive Wheat Field")
                self.field()
            elif decidelocation == 3:
                break
            else:
                print("Wrong answer try again")



    def barn(self):
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

        decide = input("There is a oddly looking creature, do you want to get close to it? y/n").lower()
        while True:
            if decide == "y":
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠄⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣉⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣈⡏⠹⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣦⡀⠀⠈⣿⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠃⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠘⣿⣤⡀⢀⡀⠀⠀⠉⠻⡟⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢉⣁⣡⣤⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣹⣿⣾⢿⣆⣠⠀⠀⢁⠈⣿⡿⠀⠈⣿⠟⠀⠈⠹⣿⡏⠀⠀⠈⣿⡟⠁⠸⣿⠃⣼⣏⢀⡆⣴⣿⣿⡟⡅⣿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣹⣿⡿⢿⣶⣷⣼⣷⣟⠁⠀⠀⡟⠀⠀⠀⠀⣽⡇⠀⠀⠀⠨⠄⠀⠀⢙⡀⢃⣸⣾⣿⣼⣿⢸⣧⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣷⡈⣷⡈⣻⣿⣼⣦⣀⣰⠃⠀⠀⠀⠀⠙⠁⠀⡀⠀⠊⣠⣀⣤⣾⣷⡌⣯⣿⢟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡺⠇⢹⣿⣿⣿⡿⣿⣤⣀⣀⣤⣤⣴⣄⠀⠃⣄⣀⢿⡿⠛⠿⣿⠙⣿⣷⣼⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⠹⣿⡿⠁⢹⡃⠈⠉⣿⠁⠊⡿⠀⠈⣿⠀⢸⡇⠀⠀⢿⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⠁⣠⣾⠇⠀⢠⣧⠀⢠⡇⠀⢀⣿⡀⢸⣇⠀⢠⣸⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣦⣠⣾⣿⣶⣾⣷⣤⣸⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("")
                print("You lost 5 hp")
                self.healthBar =- 5
                break
            elif decide == "n":
                print("The creature ran away")
                break
            else:
                print("Wrong answer try again")

        return None


    def field(self):
        print("You enter the field and you feel very sick, you can't take your time here so be quick")


        self.pl.add_item("Rotten apple")
        self.pl.add_item("Bottle of piss")

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

        print("You were about to head out from the farm but you encounter a mysterious figure")
        print("")
        print("")
        print("")
        print("Hello adventurer, I see that you're not from here and lost in this field. I can help you get out of it"
              "but you need to answer three of my riddles")
        print("But you have to be quick, or you might die to radiation poisoning")

        while True:

            print("Riddle 1: What has keys but can't open locks?")
            answer = input().lower()
            if answer == "keyboard":
                print("Correct")

            else:
                print("Wrong answer, try again")

            print("Riddle 2: What has a head, a tail, is brown, and has no legs?")
            answer = input().lower()
            if answer == "penny":
                print("Correct")

            else:
                print("Wrong answer, try again")

            print("Riddle 3: What has a neck but no head?")
            answer = input().lower()
            if answer == "bottle":
                print("Correct")
                break
            else:
                print("Wrong answer, try again")

        print("You have answered all the riddles correctly, you can now leave the field")
        print("Oh and have this as your reward")
        print("You received a mysterious fragment")
        self.pl.specialspace.append("Mysterious Fragment")

        return None

class old_nuclear_reactor(world):
    def __init__(self, Player):
        super().__init__()
        self._items = ["Old uranium rod", "Old nuclear reactor manual", "Old nuclear reactor key", "Old nuclear reactor button"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old nuclear reactor"
        self.pl = Player
        self.lvl = Level1
        self.ah = abandoned_house(Player)
        self.finished = False

    def explore_reactor(self):
        print("You decide to go to the reactor but the doors are locked")
        print("Do you want to use the rusty key? y/n")
        decide = input()

        if decide == "y":
            for i in range(len(self.pl.space)):
                if self.pl.space[i] == "Rusty key":
                    print("You use the rusty key and the door opens")
                    break
                else:
                    print("You don't have the key")
                    print("You cant go in")
                    return None
        elif decide == "n":
            print("You decide to leave the reactor")
            return None

        print("You walk in and see Dimitri again")
        print("")
        print("")
        print("")
        print("I see that you have found the old nuclear reactor")
        print("Did you find the Belurusian gold coin?")
        decide = input()

        if decide == "y":
            print("Good job. You can now go to the portal")
            print("But before you can go through, you need to answer these 3 riddles")

            while True:
                print("Riddle 1: What is the capital of Belarus?")
                answer1 = input().lower()
                if answer1 == "minsk":
                    print("Correct")
                    break
                else:
                    print("Wrong answer, try again")

            while True:
                print("Riddle 2: What is always in front of you but can’t be seen?")
                answer2 = input().lower()
                if answer2 == "future":
                    print("Correct")
                    break
                else:
                    print("Wrong answer, try again")

            while True:
                print("Riddle 3: What has to be broken before you can use it?")
                answer3 = input().lower()
                if answer3== "egg":
                    print("Correct")
                    break
                else:
                    print("Wrong answer, try again")

            print("You have answered all the riddles correctly")
            print("Here is your last piece of the puzzle")
            print("*You received the last fragment*")
            print("You can now go to the portal")
            self.finished = True

        else:
            print("Im sorry but you need to find the coin")
            print("I cant help you without it")
            return None


# run the game
if __name__ == "__main__":
    game = Level1()
    game.start()
