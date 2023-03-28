"""
    Megan Brown
    CS 5001 - Final Project
    Module for the game play
"""


import string
from typing import List, Tuple
from dice import Dice


def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command
    Options include: Play, Status, Exit
    Returns:
    Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("What would you like to do? ")
    return check.strip().casefold(), check


def run() -> None:
    """
    Runs the adventure game
    """
    menu_options = "play, status, or exit"
    command, raw = menu()

    # loop continues until user exits
    while (command != "exit"):
        if (command == "play"):
            # add game play here
            pass
        elif (command == "status"):
            # print health stats here
            pass
        else:
            print(f"Invalid command: must be {menu_options}")
        # provide the menu again
        command, raw = menu()


if __name__ == "__main__":
    run()