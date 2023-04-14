"""
    Megan Brown
    CS 5001 - Final Project
    Dice class
"""
import random


class Dice(object):
    """
    Creates Dice object
    
    Attributes: 
        name (str): the name of the dice
        sides (int): the number of sides the dice has
        sides will default to 6
    Methods:
        roll: rolls the dice
    """
    def __init__(self, name: str, sides: int = 6):
        self.__name = name
        self.__sides = sides


    @property
    def name(self) -> str:
        """
        Gets name of dice
        Args:
            self: the dice object
        Returns:
            str: The name of the dice
        """
        return self.__name


    @property
    def sides(self) -> int:
        """
        Gets number of sides
        Args:
            self: the dice object
        Returns:
            int: the number of sides the dice has
        """
        return self.__sides


    def __str__(self) -> str:
        """
        Prints info about dice object's attributes
        Args:
            self: the dice object
        Returns:
            str: Formatted string with dice name and # sides
        """
        info = "Dice name: " + self.__name + "\n" \
                "Number of sides: " + str(self.__sides)
        return info


    def roll(self) -> int:
        """
        Rolls the dice
        Args:
            self: the dice object
        Returns:
            int: the outcome/result of the roll
        """
        outcome = random.randint(1, self.__sides)
        return outcome