"""
    Megan Brown
    CS 5001 - Final Project
    Module for the game play
"""
import string
from storyline import intro
from typing import List, Tuple
from dice import Dice


def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command
    Options include: Play, Status, Exit
    Returns:
    Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("What would you like to do? (play, status, or exit) ")
    return check.strip().casefold(), check


def health_roll(impact: str) -> int:
    """
    Gets user's dice roll impacting a player's health
    Args:
        impact (str): Narrative about what this dice roll impacts
    Returns:
        int: positive int about the dice outcome
    """
    print(f"\nRoll the dice to find out {impact}.")
    kb_entry = input("Press any key to roll the dice >")
    d6 = Dice("d6")
    roll = d6.roll()
    print("\nYou rolled a", str(roll))
    return roll


def run_intro() -> dict:
    """
    Runs Part I of the adventure game
    Args:
        None
    Returns:
        Final health scores
    """
    menu_options = "play, status, or exit"
    command, raw = menu()
    health_dict = {"Robin": 100, "Martin": 100, "You": 100}

    # loop continues until user exits
    while (command != "exit"):
        if (command == "play"):
            # game play

            # part I - intro to the bee swarm
            intro()
            damage = 5
            intro_roll = health_roll("how badly Martin is stung")
            if (intro_roll >= 5):
                print("\nMartin squashed the bee against his neck, but the stinger was at an angle and managed to pop out.")
            elif (intro_roll >= 3):
                damage = damage * 2
                print("\nMartin got stung in the neck, but he managed to squash the bee that did it.")
            else:
                damage = damage * 3
                print("\nMartin is not doing well. He screams that he's allergic and his neck swell from the sting.")
            
            # update Martin's updated health score
            print(f"Damage to Martin's health: -{str(damage)}")
            original_health = health_dict["Martin"]
            new_health = original_health - damage
            health_dict["Martin"] = new_health
            return health_dict

        elif (command == "status"):
            # prints health status
            print("\nHealth Status:")
            for key, value in health_dict.items():
                player_name = key
                health = value
                if health < 0:
                    health = 0
                print(f"{player_name}: {health}%")
            
        else:
            print(f"Invalid command: must be {menu_options}")
            # provide the menu again
            command, raw = menu()
    return health_dict


def main() -> None:
    """
    Runs the adventure game
    """
    health_dict = run_intro()
    print("Current health scores:", health_dict)


if __name__ == "__main__":
    main()