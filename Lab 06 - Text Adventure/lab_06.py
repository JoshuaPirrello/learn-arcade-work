class Room:
    def __init__(self, description, north, east, south, west):
         self.description = description
         self.north = north
         self.east = east
         self.south = south
         self.west = west


def main():
    room_list = []

    room = Room(" A comfortable bedroom full of pillows", 3, 1, None, None)
    room_list.append(room)
    room = Room("A gloomy lonely hallway", 4, 2, None, 0)
    room_list.append(room)
    room = Room("A living room with a couch and static T.V.", 5, None, None, 1)
    room_list.append(room)
    room = Room("A dirty bed surrounded by random items in storage", None, 4, 0, None)
    room_list.append(room)
    room = Room("A bright hallway dotted with pictures on the wall", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("A kitchen with a sink full of dishes", None, None, 2, 4)
    room_list.append(room)
    room = Room("A bathroom! It even has a toilet!", None, None, 4, None)
    room_list.append(room)



    current_room = 0
    next_room = None

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        print("""
                A. Go North
                B. Go East
                C. Go South
                D. Go West
                Q. Quit Game""")
        print()
        userInput = input("""Make Your selection now: """)

        if userInput.upper() == "A" or userInput.upper() == "NORTH" or userInput.upper() =="N":
            next_room = room_list[current_room].north
        elif userInput.upper() == "B" or userInput.upper() =="EAST" or userInput.upper() =="E":
            next_room = room_list[current_room].east
        elif userInput.upper() == "C" or userInput.upper() =="SOUTH" or userInput.upper() == "S":
            next_room = room_list[current_room].south
        elif userInput.upper() == "D" or userInput.upper() == "WEST" or userInput.upper() == 'W':
            next_room = room_list[current_room].west
        elif userInput.upper() == "Q" or userInput.upper() == "QUIT" or userInput.upper() == "LEAVE":
            print("game over")
            break

        if next_room == None:
                print("You cannot go in this direction, you are blocked by the wall.")
        else:
            current_room = next_room
            print("You walk on ahead")

main()




