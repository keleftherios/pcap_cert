# Composition is the process of composing an object using other different objects.
# The objects used in the composition deliver a set of desired traits (properties and/or methods)
# so we can say that they act like blocks used to build a more complicated structure.
#
# It can be said that:
#
# - Inheritance extends a class's capabilities by adding new components
#   and modifying existing ones; in other words, the complete recipe is contained
#   inside the class itself and all its ancestors;
#   the object takes all the class's belongings and makes use of them;
#
# - Composition projects a class as a container able to store and use other objects
#   (derived from other classes) where each of the objects implements
#   a part of a desired class's behavior.


import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
