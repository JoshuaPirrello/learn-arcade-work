class Cat:
    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print(self.name + " says  \"Meow")


my_cat = Cat()
my_cat.name = "Zero"
my_cat.color = "black"
my_cat.weight = 8

my_cat.color = "Black"
my_cat.name = "Zero"
my_cat.age = 3

another_cat = Cat()
another_cat.color = "black"
another_cat.name = "Sniff"
another_cat.age = 4

my_cat.meow()
another_cat.meow()

class Monster:
    def __init__(self):
        self.hp = 0
        self.color = ""
        self.name = ""

    def decrease_health(self, damage):
       self.hp -= damage
       print(self.name + " has been hit!")

mush = Monster()
mush.hp = 5
mush.color = "Red"
mush.name = "Ramblin' evil Mushroom"
print(mush.name + " Has a health of " + str(mush.hp))

mush.decrease_health(2)

class Star:
    def __init__(self, name):
        self.brightness = 0
        self.age = 0
        print("A star is born and it is " + name)

star1 = Star("Solaris")
star2 = Star("Betelgeuse")

