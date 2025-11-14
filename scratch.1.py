Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... def print_divider():
...     print("\n" * 50 + "\n")
... 
... def intro():
...     print_divider()
...     print("WELCOME TO THE QUEST ENGİNE")
...     print("A story-driven adventure where every choice matters.")
...     print("Your Journey begins now...")
...     print_divider()
... 
...     name = input("Traveler what is your name?")
...     print(f"\nGreetings, {name}. Your destiny awaits...\n")
...     return name
... 
... def choose_path(name):
...     print("You arrive at a crossroads in an ancient forest.")
...     print("Two paths lie ahead:")
...     print("1) The paths Wisdom (Puzzle-Based)")
...     print("2) the paths courage (Battle simulation")
... 
...     choice = input("which path will you take? (1 or 2): ")
... 
...     if choice == "1":
...         return path_of_wisdom(name)
...     elif choice == "2":
...         return path_of_courage(name)
...     else:
...         print("İnvalid choice. Fate rejects your hesitation.")
...         return choose_path(name)
... 
... def path_of_wisdom(name):
...     print_divider()
...     print("You step into the path courage...")
...     print("A shadowy creature approaches!")
... 
...     player_hp = 30
...     monster_hp = 20

    while player_hp > 0 and monster_hp > 0:
        print_divider()
        print(f"Your HP: {player_hp}")
        print(f" Monster HP: {monster_hp}")

        action = input ("Do you attack (a) or defend (d)?")

        if action == "a":
            print("\nYou strike the creature!")
            monster_hp -= 10
        elif action == "d":
            print("\nYpu brace yourself. The attack hurts less.")
            player_hp -= 3
        else:
            print("\nYou hesitate. The creature attacks!")
            player_hp -= 7
        if monster_hp > 0:
            print("The creature claws at you!")
            player_hp -= 5

    if player_hp <= 0:
        print("\nYou fall in battle... but courage never dies.")
        ending(name, "Fallen Hero")
    else:
        print("\nYou defeated the monster! Victory is yours!")
        ending(name, "Courage")

def ending(name, path):
    print_divider()
    print(f"THE END - {path} Ending")
    print(f"Well done, {name}. Your story is written in the stars.")
    print("This is only te beginning...")
    print_divider()

def main():
    name = intro()
    choose_path(name)

main()





