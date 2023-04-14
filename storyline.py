"""
Megan Brown
CS 5001 - Final Project
File for story narrative elements
"""


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
    choice = input("Your options ('state concern', 'continue')")
    if choice.strip() == 'state concern':
        print("\nYou: Hey, do you hear that sound?...")
        print("Robin: I do.. it's weird. I wonder what it is.")
    print("\nYour car continues along the road further into nature.")
    choice = input("Your options ('continue', 'pull over')")
    if choice.strip() == 'pull over':
        print("Robin pulls over and stops the car.")
    print("\nMartin swats at his neck.")
    print("Martin: Ahhh I think I've been stung...")
    choice = input("Your options ('look')")
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
    choice = input("Your options for moving ('slow', 'fast')")
    if choice.strip() == 'slow':
        print("\nYou slowly unbuckle and slip out of the car.")
        print("You do not draw any attention to yourself from the swarm.")
    if choice.strip() == 'fast':
        print("\nYou quickly unbuckle and hop out of the car.")
        print("You're ready to run.")
    print("\nYou run as fast as you can. You have to get away.")
    print("There's a trail through the trees, and there's the paved road ahead.")
    choice = input("Your options ('trail', 'road')")
    if choice.strip() == 'trail':
        print("\nYou dart down the trail through the trees.")
        print("Branches scrape your arm as you run.")
    if choice.strip() == 'road':
        print("\nYou stick to the paved road, running where cars can see you.")
    print("\nThere's a fork in the road. Which way do you go?")
    choice = input("Your options ('left', 'right')")
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
    choice = input("Your options ('help', 'watch')")
    while choice.strip() == 'watch':
        print("\nMartin and Robin scream: 'Help!!'")
        choice = input("Your options ('help', 'watch')")
    print("\nYou run up to your friends to help. Bees begin to swarm you.")
    print("Robin: Pull your shirt over your face to cover your eyes and mouth.")
    choice = input("Choose face protection ('tshirt', 'nothing')")
    while choice.strip() == 'nothing':
        print("\nBees swarm your face and target your eyes and mouth.")
        choice = input("Choose face protection ('tshirt', 'nothing')")
    print("\nYou protect your face by pulling your shirt up to cover it.")
    print("\nYou see a hose on the ground...")
    choice = input("Your options ('spray', 'nothing')")
    while choice.strip() == 'nothing':
        print("\nThe bees continue to attack your group.")
        choice = input("Your options ('spray', 'nothing')")
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
    choice = input("Your choice ('ask')")
    if (choice.strip() == "ask"):
        print("\nYou: What was that?")
        print("Beekeeper: Killer bees took over my hive. I tried to kill the queen today, but it went very badly.")