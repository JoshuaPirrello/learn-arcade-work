import random


def main():
    print("Welcome to Camel")
    print("You have stolen a camel to make your way across the great Mobi desert")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.\n")

    #define variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel = tiredness = 0
    natives_traveled = -20
    canteen = 3


    while done == False:
        print("""A. Drink from your canteen
B. Ahead Moderate speed
C. Ahead Full speed
D. Stop for the night
E. status check
Q. Quit""")
        break
    if thirst > 4:
        print("\nYou are thirsty\n")

    user_choice = input("What is your choice?")

    # game logic follows

    if user_choice.upper() == "Q":
        print("You have left the game.")
    elif user_choice.upper()== "E":
        print("\n You have traveled" + str(miles_traveled) + "miles.")
        print("You have" + str(canteen) + "drinks left")
        print("The natives are" + str(miles_traveled - natives_traveled) + "miles behind you\n")
    elif user_choice.upper()== "D":
        print("\n You have stopped for the night to rest.")
        print("Your camel is rested and looks content!")
        natives_traveled=natives_traveled+random.randrange(7,14)
        print("The natives are" + str(miles_traveled - natives_traveled) + "miles behind you\n")
    elif user_choice.upper()== "C":
        thirst=thirst+1
        print("\n Your camel runs like the wind")
        miles_traveled=miles_traveled+random.randrange(10,20)
        camel_tiredness=camel+random.randrange(1,3)
        natives_traveled = natives_traveled + random.randrange(7, 14)
        print("The natives are" + str(miles_traveled - natives_traveled) + "miles behind you\n")
    elif user_choice.upper()== "B":
        thirst = thirst + 1
        print("\n Your camel moseys down the desert.")
        miles_traveled = miles_traveled + random.randrange(4, 11)
        natives_traveled=natives_traveled+random.randrange(7,14)
        print("The natives are" + str(miles_traveled - natives_traveled) + "miles behind you\n")
    elif user_choice.upper()== "A":
        if canteen>0:
            thirst = 0
        canteen=canteen - 1
        print("How refreshing!")
    else:
        print("You are out of water")

    if thirst > 6:
        print("\nYou have died of thirst\n")
        done = True
    if miles_traveled > 199:
        print("\n You have traveled across the desert alive.\n")
        done = True



main()
