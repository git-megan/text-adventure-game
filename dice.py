"""
    Megan Brown
    CS 5001 - Final Project
    Dice class
"""
import random


class Dice(object):
    """
    Attributes: name, sides
    Methods: roll
    """
    def __init__(self, name: str, sides: int = 6):
        self.__name = name
        self.__sides = sides


    @property
    def name(self) -> str:
        # gets name of dice
        return self.__name


    @property
    def sides(self) -> int:
        # gets number of sides
        return self.__sides


    def __str__(self) -> str:
        # prints info about dice object
        info = "Dice name: " + self.__name + "\n" \
                "Number of sides: " + str(self.__sides)
        return info


    def roll(self) -> int:
        # rolls the dice
        outcome = random.randint(1, self.__sides)
        return outcome