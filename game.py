"""
Megan Brown
CS 5001 - Final Project
Module for the game play
"""
from typing import Tuple
import storyline
from scene import Scene


def get_title() -> str:
    """
    Gets the title sequence string
    Args:
        None
    Returns:
        str: The title and subtitle of the game
    """
    title = "\nEscape of the Bees"
    subtitle = "\nA text adventure game by Megan Brown"
    return title + subtitle


def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command
    Options include: Play, Status, Exit
    Returns:
    Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("\nGame Menu: What would you like to do? (play, status, or exit) ")
    return check.strip().casefold(), check


def get_status(scores_dict: dict) -> str:
    """
    Gets the players' health scores
    Args:
        scores_dict (dict): A dictionary with the player name as key, and health as value
    Returns:
        str: player's health scores in a formatted string
    """
    status = "\nHealth Status:"
    for key, value in scores_dict.items():
        player_name = key
        health = value

        # ensure no negative health percentages
        if health < 0:
            health = 0
        
        # add new line for player's health as a percentage
        status += f"\n{player_name}: {health}%"
    return status


def update_scores(scores_dict: dict, player: str, damage: int) -> dict:
    """
    Updates the player's health scores
    Args:
        scores_dict (dict): A dictionary with the original health scores
        player (str): The player(s) taking the damage
        (Can be the name of one player or 'everyone')
        damage (int): The amount of damage to deduct from the player(s)
    Returns:
        dict: A dictionary with the updated health scores
    """
    if player != "everyone":
        # update single player's health score
        if player in scores_dict:
            scores_dict[player] = scores_dict[player] - damage
        else:
            # if necessary, create a new entry for a new player
            scores_dict[player] = 100 - damage
    else:
        # update everyone's health score
        for key, value in scores_dict.items():
            scores_dict[key] = value - damage
    return scores_dict


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


def run_part(my_scene: Scene, health_dict: dict) -> Tuple[dict, str]:
    """
    Runs a narrative and scene of the adventure game
    Args:
        my_scene (Scene): The scene object to play
        health_dict (dict): A dict with the current health scores of players
    Returns:
        Tuple[dict, str]: Health scores after playing this scene, menu command
        (e.g. ({"Robin": 100, "Martin": 95, "You": 80}, "exit"))
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

            # update health score
            new_health_scores = update_scores(health_dict, player, damage)

            return new_health_scores, command

        elif (command == "status"):
            # get and print health status
            health_status = get_status(health_dict)
            print(health_status)
            command, raw = menu()

        else:
            print(f"Invalid command: must be {menu_options}")
            # provide the menu again
            command, raw = menu()
    return health_dict, command


def create_scenes() -> Tuple[Scene, Scene, Scene]:
    """
    Instantiates the scenes for this game
    Args:
        None
    Returns:
        Tuple[Scene, Scene, Scene]: All of the scenes for the game
    """
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
    good_outcome_1 = ("Luckily no bees have followed you, but you're arm got cut during the run.", 3)
    bad_outcome_1 = ("A loud buzz rings in your ears.\nYou swat at your face, but it's too late, you've been stung.", 10)

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

    # return tuple of scenes
    return intro_scene, part_2_scene, part_3_scene


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
    print(get_title())

    # initialize game scenes
    game_scenes = create_scenes()

    # saves scores each time a scene runs
    health_scores = {"Robin": 100, "Martin": 100, "You": 100}

    # run part I - intro
    health_scores, command = run_part(game_scenes[0], health_scores)

    # run part II - escape
    if (command != "exit"):
        health_scores, command = run_part(game_scenes[1], health_scores)
 
        # run part III - help friends
        if (command != "exit"):
            health_scores, command = run_part(game_scenes[2], health_scores)

            # resolution - bee keeper reveals context
            if (command != "exit"):
                storyline.resolution()
                print("\nThe end... You survived!! 🎉")


if __name__ == "__main__":
    main()