print('Your pirate ship is running away from the enemy. You can sail into a storm, past a monster, or turn around and fight. Which option do you take?')
option = input('Choose storm, monster, or fight (one option and lowercase only please): ') 
if option == 'storm':
    print("The elements are against you. A huge hole is torn in your mainsail. What do you do next?")
    print("1. Abandon ship.")
    print("2. Send men to repair the sail.")
    sail = input("Enter 1 or 2: ")
    if sail == "1":
            print("So sorry. You drown at sea.")
    else:
        print("Your bravery is rewarded. The sail is repaired and you make it through the storm!")
        print("Now what?")
        print("1. Keep heading forward even though you have no idea where you are.")
        print("2. Steer back home and call this thing a bust.")
        option = input("Enter 1 or 2: ")
        if option == "1":
            print("Aaaaand you ran out of food. You're dead.")
        else:
            print("You tried to turn towards home but stayed lost at sea anyways. Sorry.")
elif option == 'monster':
    print("The monster is too strong and you start to be drawn toward it. What do you do next?")
    print("1. Steer really hard in the opposite direction.")
    print("2. Sacrifice a few men to the monster.")
    monster = input("Enter 1 or 2: ")
    if monster == "1":
            print("Nice try, but that monster got you anyway!")
    else:
        print("Sad about those fellows, but at least you and the rest of the crew made it out alive.")
        print("Now what?")
        print("1. Sail to the South of France!")
        print("2. Give up and turn around.")
        option = input("Enter 1 or 2: ")
        if option == "1":
            print("Congrats! Enjoy yourself before you run out of money.")
        else:
            print("You crash landed in Hawaii and everybody loves you!")

elif option == 'fight':
    print("The enemy is powerful and they begin to overwhelm you. What do you do next?")
    print("1. Throw a giant grenade at the enemy, chancing it will blow up your ship also.")
    print("2. Surrender.")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
            print("Oops. You blew everyone up. Nice work.")
    else:
        print("Huh, that worked out. Turns out the enemy is super nice. They give you comfy bunks and lots of food.")
        print("Now what?")
        print("1. Stay with the monster and live happily for the rest of your days.")
        print("2. Decide to go back home to your family.")
        option = input("Enter 1 or 2: ")
        if option == "1":
            print("You travel the world and have never been happier!")
        else:
            print("The enemy catches up to you again and decides to destroy you anyways.")

else: 
    print("Can't make up your mind? Not good. You're toast one way or another!")
        

