"""
    Megan Brown
    CS 5001 - Final Project
    Dice class
"""
import random


class Dice:
    def __init__(self, name: str, sides: int = 6) -> None:
        """
        Creates Dice object
    
        Attributes: 
            name (str): the name of the dice
            sides (int): the number of sides the dice has
            sides will default to 6
        Methods:
            roll: rolls the dice
        """
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
    

    def health_roll(self, impact: str) -> int:
        """
        Gets user's dice roll impacting a player's health
        This method also prints what's going on in the game
        (e.g. 'Roll the dice to find out what happens to Martin.')
        
        Args:
            self: the dice object
            impact (str): Narrative about what this dice roll impacts
        Returns:
            int: positive int about the dice outcome
        """
        print(f"\nRoll the dice to find out {impact}.")
        kb_entry = input("Press ENTER to roll the dice >")
        roll = self.roll()
        print("\nYou rolled a", str(roll))
        return roll