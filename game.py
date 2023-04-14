"""
    Megan Brown
    CS 5001 - Final Project
    Module for the game play
"""
import string
from storyline import intro, part_2, part_3, resolution
from typing import List, Tuple
from dice import Dice


def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command
    Options include: Play, Status, Exit
    Returns:
    Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("\nGame Menu: What would you like to do? (play, status, or exit) ")
    return check.strip().casefold(), check


def print_status(scores_dict: dict) -> None:
    """
    Prints the players' health scores in a formatted way
    Args:
        scores_dict (dict): A dictionary with the player name as key, and health as value
    Returns:
        None
    """
    print("\nHealth Status:")
    for key, value in scores_dict.items():
        player_name = key
        health = value

        # ensure no negative health percentages
        if health < 0:
            health = 0
        
        # prints health as a percentage
        print(f"{player_name}: {health}%")


def health_roll(impact: str) -> int:
    """
    Gets user's dice roll impacting a player's health
    Args:
        impact (str): Narrative about what this dice roll impacts
    Returns:
        int: positive int about the dice outcome
    """
    print(f"\nRoll the dice to find out {impact}.")
    kb_entry = input("Press ENTER to roll the dice >")
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
                print("\nMartin is not doing well. He screams that he's allergic. His neck swells from the sting.")
            
            # update Martin's health score
            print(f"Damage to Martin's health: -{str(damage)}")
            original_health = health_dict["Martin"]
            new_health = original_health - damage
            health_dict["Martin"] = new_health
            return health_dict

        elif (command == "status"):
            # prints health status
            print_status(health_dict)
            command, raw = menu()
            
        else:
            print(f"Invalid command: must be {menu_options}")
            # provide the menu again
            command, raw = menu()
    
    return health_dict


def run_part_2(saved_scores: dict) -> dict:
    """
    Runs Part II of the adventure game
    Args:
        saved_scores (dict): Dictionary of health scores from playing the intro
    Returns:
        dict: Dictionary of health scores from playing Part II
    """
    health_dict = saved_scores
    menu_options = "play, status, or exit"
    command, raw = menu()
    
    # loop continues until user exits
    while (command != "exit"):
        if (command == "play"):
            # game play
            # part II - escape the bees
            part_2()
            damage = 0
            part_2_roll = health_roll("if any bees have followed you")
            if (part_2_roll > 3):
                damage += 2
                print("\nLuckily no bees have followed you. You're in the clear.")
                print("\nUnfortunately, your arm got scratched while running.")
            else:
                damage += 15
                print("\nA loud buzz rings in your ears.\nYou swat at your face, but it's too late, you've been stung.")
            # update health score
            print(f"Damage to your health: -{str(damage)}")
            original_health = health_dict["You"]
            new_health = original_health - damage
            health_dict["You"] = new_health
            choice = input("\nPress ENTER to continue >")
            print("\nMeanwhile... your friends need you.")
            return health_dict

        elif (command == "status"):
            # prints health status
            print_status(health_dict)
            command, raw = menu()

        else:
            print(f"Invalid command: must be {menu_options}")
            # provide the menu again
            command, raw = menu()
    return health_dict


def run_part_3(saved_scores: dict) -> dict:
    """
    Runs Part III of the adventure game
    Args:
        saved_scores (dict): Dictionary of health scores from playing the intro
    Returns:
        dict: Dictionary of health scores from playing Part III
    """
    health_dict = saved_scores
    menu_options = "play, status, or exit"
    command, raw = menu()
    
    # loop continues until user exits
    while (command != "exit"):
        if (command == "play"):
            # game play
            # part III - help friends
            part_3()
            damage = 0
            part_3_roll = health_roll("if your group out ran the bees")
            if (part_3_roll > 2):
                print("\nEveryone made it safely inside the stranger's house.")
            else:
                damage += 20
                print("\nThe bees swarm and sting you as your run, but you make it inside the house.")
                # update health scores for everyone in group
                print(f"Damage to your group's health: -{str(damage)}")
                for player, health in health_dict.items():
                    new_health = health - damage
                    health_dict[player] = new_health
            
            choice = input("\nPress ENTER to continue >")
            return health_dict

        elif (command == "status"):
            # prints health status
            print_status(health_dict)
            command, raw = menu()
       
        else:
            print(f"Invalid command: must be {menu_options}")
            # provide the menu again
            command, raw = menu()
    return health_dict


def main() -> None:
    """
    Runs the adventure game
    
    Health scores are saved at each chapter 
    and passed on to the next chapeter

    Args:
        None
    Returns:
        None
    """
    print("\nEscape of the Bees")
    print("A text adventure game by Megan Brown")
    # run part I - intro
    health_dict_1 = run_intro()
    
    # save scores
    final_scores = health_dict_1

    #current game ending str
    end_message = "\nThe end... 🐝"

    # run part II - escape
    martin_health = health_dict_1["Martin"]
    if (martin_health != 100):
        health_dict_2 = run_part_2(health_dict_1)
        final_scores = health_dict_2
        
        # run part III - help friends
        your_health = health_dict_2["You"]
        if (your_health != 100):
            final_scores = run_part_3(health_dict_2)
            end_message = "\nThe end... You survived!! 🎉"
    
        # resolution - bee keeper reveals context
        # this plays for all endings/exits of the game
        resolution()

    print(end_message)


if __name__ == "__main__":
    main()