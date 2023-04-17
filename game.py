"""
Megan Brown
CS 5001 - Final Project
Module for the game play
"""
from typing import Tuple
import storyline
from scene import Scene


def run_title() -> None:
    """
    Runs the title sequence (v1: prints title)
    Args:
        None
    Returns:
        None
    """
    print("\nEscape of the Bees")
    print("A text adventure game by Megan Brown")


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


def play_narrative(my_scene: Scene) -> None:
    """
    Prints the interactive narrative corresponding to the scene
    Args:
    my_scene (Scene): The scene that the narrative is for
    Returns:
    None
    """
    scene_title = my_scene.name
    if (scene_title == "intro"):
        storyline.intro()
    elif (scene_title == "part_2"):
        storyline.part_2()
    elif (scene_title == "part_3"):
        storyline.part_3()


def run_part(my_scene: Scene, health_dict: dict) -> dict:
    """
    Runs a narrative and scene of the adventure game
    Args:
        my_scene (Scene): The scene object to play
        health_dict (dict): A dict with the current health scores of players
    Returns:
        dict: Health scores after playing this scene
    """
    command, raw = menu()
    menu_options = "play, status, or exit"

    # loop continues until user exits
    while (command != "exit"):
        if (command == "play"):
            # game play
            # play narrative intro
            play_narrative(my_scene)
            # play the scene, get dice roll damage outcome
            player, damage = my_scene.play()

            # update player's health score
            print(f"Damage to health: -{str(damage)}")
            if player != "everyone":
                # update single player's health score
                health_dict[player] = health_dict[player] - damage
            else:
                # update everyone's health score
                for key, value in health_dict.items():
                    health_dict[key] = value - damage
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
    # prints title of game
    run_title()

    # initialize game scenes
    # To initialize, first create variables for scene objects
    name_0 = "intro"
    impact_0 = "how badly Martin is stung"
    player_0 = "Martin"
    cut_off_0 = 3
    good_outcome_0 = ("Martin squashed the bee against his neck, but the stinger was at an angle and managed to pop out.", 5)
    bad_outcome_0 = ("Martin screams that he's allergic. His neck swells from the sting.", 15)

    name_1 = "part_2"
    impact_1 = "if any bees have followed you"
    player_1 = "You"
    cut_off_1 = 4
    good_outcome_1 = ("Luckily no bees have followed you, but you're arm got cut during the run.", 5)
    bad_outcome_1 = ("A loud buzz rings in your ears.\nYou swat at your face, but it's too late, you've been stung.", 15)

    name_2 = "part_3"
    impact_2 = "if your group out ran the bees"
    player_2 = "everyone"
    cut_off_2 = 3
    good_outcome_2 = ("Everyone made it safely inside the stranger's house.", 0)
    bad_outcome_2 = ("The bees swarm and sting you as your run, but you make it inside the house.", 20)

    # create scene objects
    intro_scene = Scene(name_0, impact_0, player_0, cut_off_0, good_outcome_0, bad_outcome_0)
    part_2_scene = Scene(name_1, impact_1, player_1, cut_off_1, good_outcome_1, bad_outcome_1)
    part_3_scene = Scene(name_2, impact_2, player_2, cut_off_2, good_outcome_2, bad_outcome_2)

    # saves scores each time a scene runs
    health_scores = {"Robin": 100, "Martin": 100, "You": 100}
    
    # run part I - intro
    health_scores = run_part(intro_scene, health_scores)

    # run part II - escape
    if (health_scores["Martin"] != 100):
        health_scores = run_part(part_2_scene, health_scores)
        
        # run part III - help friends
        if (health_scores["You"] != 100):
            health_scores = run_part(part_3_scene, health_scores)

        # resolution - bee keeper reveals context
        storyline.resolution()
        print("\nThe end... You survived!! 🎉")


if __name__ == "__main__":
    main()