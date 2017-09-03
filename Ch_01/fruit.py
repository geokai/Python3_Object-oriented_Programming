"""This module contains the fruit class and sub-classes.

Python3 OOP - Chapter 1, Apples & Oranges
"""


# This file was created on 02/09/2017
# Author: George Kaimakis - https://github.com/geokai


class Fruit:
    """General fruit class"""
    num_of_fruit = 0

    def __init__(self, pick_date):
        self.pick_date = pick_date
        Fruit.num_of_fruit += 1

    def get_num_fruit(self):
        """returns the number of fruits"""
        return self.num_of_fruit

    def add_to_container(self):
        """adds fruit to the appropriate container"""

class Apple(Fruit):
    """Apple class"""
    num_of_apples = 0

    def __init__(self, pick_date, color):
        super().__init__(pick_date)
        self.color = color
        self.num_of_apples += 1

    def get_color(self):
        """returns the color of the apple"""
        return self.color


class Orange(Fruit):
    """Orange class"""
    num_of_oranges = 0

    def __init__(self, pick_date, size):
        super().__init__(pick_date)
        self.size = size
        self.num_of_oranges += 1

    def get_size(self):
        """returns the size of the orange"""
        return self.size
