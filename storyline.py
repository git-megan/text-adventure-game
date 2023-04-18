"""
Megan Brown
CS 5001 - Final Project
File for story narrative elements

Storylines will create the illusion that the player is making choices
However, all storyline functions are for narrative purposes only
"""


def clean_string(my_str: str) -> str:
    """
    Turns str into cleaned up version
    Out put doesn't have whitespace and is lower case

    Args:
        my_str (str): original str
    Returns:
        str: cleaned up str
    """
    return my_str.strip().casefold()


def get_choice(choices: list, more_context: str = "") -> int:
    """
    Asks user to choose a path that impacts the story
    Requires a choice to continue
    Args:
        choices (list): list of strings which are choice options
        more_context(str): Provides more context on what they are choosing
        (e.g. "getting out of the car")
    Returns:
        int: index of the choice the user made
    """
    # placeholder for choice options str
    options_str = ""

    # clean up choice strings to remove spaces and caps
    for i in range(len(choices)):
        choice = clean_string(choices[i])
        # build str to share choices with user
        if i != (len(choices) - 1):
            options_str += f"'{choice}', "
        else:
            options_str += f"'{choice}'"
        # save cleaned up str in choices list
        choices[i] = choice

    # build str to ask for user's choice
    ask = f"Your options ({options_str})"
    
    # use more context, if str provided
    if (more_context != ""):
        ask = f"Your options for {more_context} ({options_str})"

    user_choice = clean_string(input(ask))
    while (user_choice not in choices):
        user_choice = clean_string(input(ask))
    return choices.index(user_choice)


def intro() -> None:
    """
    Intro storyline
    Sets the scene for the bee swarm
    Args:
        None
    Returns:
        None
    """
    print("\nPart I - Intro")
    print("\nYou are driving to Marin in a convertable with your two friends - Martin and Robin.")
    print("It's a wonderful day, but all of a sudden you hear a buzzing sound growing louder.")
    choice = get_choice(["state concern", "continue"])
    if choice == 0:
        print("\nYou: Hey, do you hear that sound?...")
        print("Robin: I do.. it's weird. I wonder what it is.")
    print("\nYour car continues along the road further into nature.")
    choice = get_choice(["pull over", "continue"])
    if choice == 0:
        print("Robin pulls over and stops the car.")
    print("\nMartin swats at his neck.")
    print("Martin: Ahhh I think I've been stung...")
    choice = get_choice(["look"])
    if choice == 0:
        print("\nYou peer back at Martin.")
        print("He's swelling around his neck, and a large swarm of bees is approaching.")


def part_2() -> None:
    """
    Part II of storyline
    Narrative for running away from the bees
    Args:
        None
    Returns:
        None
    """
    print("\nPart II - The Escape")
    print("\nYou realize you need to get out of this situation.")
    print("You move to get out of the car")
    choice = get_choice(["slow", "fast"], "moving")
    if choice == 0:
        print("\nYou slowly unbuckle and slip out of the car.")
        print("You do not draw any attention to yourself from the swarm.")
    if choice == 1:
        print("\nYou quickly unbuckle and hop out of the car.")
        print("You're ready to run.")
    print("\nYou run as fast as you can. You have to get away.")
    print("There's a trail through the trees, and there's the paved road ahead.")
    choice = get_choice(["trail", "road"])
    if choice == 0:
        print("\nYou dart down the trail through the trees.")
        print("Branches scrape your arm as you run.")
    if choice == 1:
        print("\nYou stick to the paved road, running where cars can see you.")
    print("\nYou keep running, and then stop to look back.")
    print("Did you out run the swarm?")


def part_3() -> None:
    """
    Part III of the storyline
    Narrative for helping your friends survive
    Args:
        None
    Returns:
        None
    """
    print("\nPart III - Facing the Swarm")
    print("\nYou run back to help your friends.")
    print("Your friends are being circled by a swarm of angry bees.")
    choice = get_choice(["help", "watch"])
    while choice == 1:
        print("\nMartin and Robin scream: 'Help!!'")
        choice = get_choice(["help", "watch"])
    print("\nYou run up to your friends to help. Bees begin to swarm you.")
    print("Robin: Pull your shirt over your face to cover your eyes and mouth.")
    choice = get_choice(["tshirt", "nothing"], "face protection")
    while choice == 1:
        print("\nBees swarm your face and target your eyes and mouth.")
        choice = get_choice(["tshirt", "nothing"], "face protection")
    print("\nYou protect your face by pulling your shirt up to cover it.")
    print("\nYou see a garden hose on the ground...")
    choice = get_choice(["spray", "nothing"], "the hose")
    while choice == 1:
        print("\nThe bees continue to attack your group.")
        choice = get_choice(["spray", "nothing"], "the hose")
    print("\nYou spray the hose in the air and at your faces, keeping the bees away.")
    print("\nMartin: Hey - there's someone at the door of that house there...")
    print("Robin: Let's make a run for it.")


def resolution() -> None:
    """
    Storyline for the resolution of the game
    Bee keeper arrives and reveals context
    Args:
        None
    Returns:
        None
    """
    print("\nA woman in a beekeeper suit comes by.")
    print("She's holding a basket of epipens and offers it to you.")
    print("You want to ask her what is going on.")
    choice = get_choice(["ask", "nothing"], "interaction")
    if choice == 0:
        print("\nYou: What was that?")
        print("Beekeeper: Killer bees took over my hive. I tried to kill the queen today, but it went very badly.")