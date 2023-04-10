"""
Megan Brown
CS 5001 - Final Project
File for story narrative elements
"""


def intro():
    print("\nYou are driving to Marin a convertable with your two friends - Martin and Robin.")
    print("It's a wonderful day, but all of a sudden you hear a buzz sound growing louder.")
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


def part_2():
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