import turtle

"""from test_function import *

user = input("What is your username: ")
greet_user(user)"""

class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        self.interior_angles = (self.sides-2)*180
        self.angle = 180-self.interior_angles/self.sides

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(self.angle)
        turtle.done()

square = Polygon(4,"Square")
pentagon = Polygon(5,"Pentagon")

"""print(square.sides)
print(square.name)
print(pentagon.interior_angles)
print(pentagon.angle)

pentagon.draw()"""

"""alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

print(alien_0)
print(len(alien_0))"""

"""name = input("What's your name? ")
print(f"Hello, {name}.")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("\nYou can vote!")
else:
    print("\nYou can't vote yet.")

tip = input("How much do you want to tip? ")
tip = float(tip)"""

