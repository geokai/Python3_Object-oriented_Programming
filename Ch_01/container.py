"""This module contains the container class and sub-classes.

Python3 OOP - Chapter 1, Apples & Oranges
"""


# This file was created on 02/09/2017
# Author: George Kaimakis - https://github.com/geokai


class Container(object):
    """Container class"""
    containers = []
    num_of_cntnrs = 0

    def __init__(self, start_date):
        self.start_date = start_date
        self.containers.append(self)
        Container.num_of_cntnrs = len(Container.containers)

    def ship_container(self):
        """marks the container as 'shipped' and sets the date of shipping"""

    def get_num_of_containers(self):
        """return the number of containers"""
        Container.num_of_cntnrs = len(Container.containers)
        return self.num_of_cntnrs

    def is_full(self):
        """return whether container is full"""

    def add_fruit(self):
        """adds a fruit to the container - apple -> barrel | orange -> basket"""
        # print('fruit added to container')


class Barrel(Container):
    """creates a barrel object with creation date and size of barrel"""
    num_of_barrels = 0

    def __init__(self, start_date, size):
        super().__init__(start_date)
        self.size = size
        Barrel.num_of_barrels += 1

    def get_size(self):
        """returns the size of the barrel"""
        return self.size

    def get_num_of_barrels(self):
        """returns the number of barrels"""
        return self.num_of_barrels


class Basket(Container):
    """creates a basket object with creation date and if cover exists"""
    num_of_baskets = 0

    def __init__(self, start_date, has_cover=False):
        super().__init__(start_date)
        self.has_cover = has_cover
        Basket.num_of_baskets += 1

    def is_covered(self):
        """returns if the basket has a cover"""
        return self.has_cover

    def add_cover(self):
        """adds a cover to the basket"""
        self.has_cover = True

    def get_num_of_baskets(self):
        """returns the number of baskets"""
        return self.num_of_baskets
