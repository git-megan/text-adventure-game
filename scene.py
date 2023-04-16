"""
Megan Brown
CS 5001 - Final Project
Scene class
"""
from typing import Tuple
from game import health_roll


class Scene(object):
    def __init__(self, name: str, impact: str, player: str, cut_off: int, outcomes: dict) -> None:
        """
        Creates Scene object
        A scene allows the client to be told what might happen, roll the dice, and find out what happens

        Attributes:
            name (str): the name of the scene (e.g. intro, part_1)
            impact (str): what will happen as a result of the dice roll
            player (str): which player is impacted
            cut_off (int): the lowest dice roll for a good outcome
            outcomes (dict): dict containing story str and damage int for good and bad outcomes
                    e.g. outcomes = {"good": ("this happened", 2), "bad":("that happened", 15)}

        Methods:
            play: plays the scene, returns damage outcomes
        """
        self.__name = name
        self.__impact = impact
        self.__player = player
        self.__cut_off = cut_off
        self.__outcomes = outcomes
    

    @property
    def name(self) -> str:
        return self.__name


    @property
    def impact(self) -> str:
        return self.__impact
    

    @property
    def player(self) -> list:
        return self.__player
    

    @property
    def cut_off(self) -> int:
        return self.__cut_off
    

    @property
    def outcomes(self) -> int:
        return self.__outcomes
    

    def __str__(self) -> str:
        """
        Prints info about scene object's attributes
        Args:
            self: the scene object
        Returns:
            str: Formatted string with scene name, players, and impact
        """
        players_str = ""
        # build str for players impacted by scene 
        for name in self.__players:
            players_str += name + ' '

        info = "Scene name: " + self.__name + "\n" \
                "Impact: " + self.__impact + "\n" \
                "Players impacted: " + players_str.strip()
        return info
    

    def play(self) -> Tuple[str,int]:
        """
        Plays the scene
        Args:
            self: the scene object
        Returns:
            result (tuple): the player impacted, health damage
                e.g. ("Martin", 15)
        """
        # positive damage to player's health
        damage = 0

        # roll dice to find out the damage and outcome
        scene_roll = health_roll(self.__impact)
        # temporary str for the outcome
        outcome = "something happened"

        # find out the result of the dice roll
        if (scene_roll >= self.__cut_off):
            outcome = self.__outcomes[good][0]
            damage += self.__outcomes[good][1]
        else:
            outcome = self.__outcomes[bad][0]
            damage += self.__outcomes[bad][1]

        # print what just happened as a result of the dice roll
        print(f"\n{outcome}")

        # returns a tuple of player impacted, health damage
        result = (self.__player, damage)
        return result
