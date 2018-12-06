import random

""" Creates a car object that can move forward
    proportionately to its horse power"""


class Car:

    def __init__(self, name, brand, color, horse_power):
        self.distance_covered = 0
        self.name = name
        self.brand = brand
        self.color = color
        self.horse_power = horse_power

    def move_forward(self):
        luck = random.random()
        self.distance_covered += luck * self.horse_power

    def get_name(self):
        return self.color + " " + self.brand + " " + self.name

    def get_distance_covered(self):
        return self.distance_covered
