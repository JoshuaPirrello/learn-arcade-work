import random

def main():
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    canteen = 3

    print("Welcome to Camel")
    print("You have stolen a camel to make your way across the great Mobi desert")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.\n")

    while not done:
        print("""
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.""")
        print()
        userInput = input("Make your choice: ")

        if userInput.upper() == "Q":
            done = True
            print("You have left the game.")

        elif userInput.upper()== "E":
                print("\n You have traveled " + str(miles_traveled) + " miles. ")
                print("You have " + str(canteen) + " drinks left")
                print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you \n")

        elif userInput.upper()== "D":
                print("\n You have stopped for the night to rest.")
                print("Your camel is rested and looks content!")
                natives_traveled = natives_traveled + random.randrange(7,14)
                print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you \n")

        elif userInput.upper()== "C":
            thirst += 1
            print("\n Your camel runs like the wind")
            miles_traveled = miles_traveled + random.randrange(10,20)
            camel_tiredness += random.randrange(1,3)
            natives_traveled = natives_traveled + random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you \n")
            check_for_oasis()

        elif userInput.upper()== "B":
            thirst = thirst + 1
            print("\n Your camel moseys down the desert.")
            miles_traveled = miles_traveled + random.randrange(4, 11)
            natives_traveled=natives_traveled + random.randrange(7,14)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you \n")
            check_for_oasis()

        elif userInput.upper()== "A":
            if canteen>0:
                thirst = 0
            canteen=canteen - 1
            print("How refreshing!")
        else:
            print("You are out of water")


            if thirst > 6:
                print("\nYou have died of thirst\n")
                done = True
            if miles_traveled >= 200:
                print("\n You have traveled across the desert alive.\n")
                done = True
            if natives_traveled <= 15:
                print("The natives are coming!")
            if natives_traveled >= miles_traveled:
                print("The natives caught and beheaded you.")
                print("You're dead!")
                done = True

def check_for_oasis():
    lucky_number = random.randrange(1,21)
    if lucky_number == 10:
        camel_tiredness = 0
        thirst = 0
        canteen = 3
        print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")

main()
