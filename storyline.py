"""
Megan Brown
CS 5001 - Final Project
File for story elements
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
    print("He's swelling around his neck, and a large swarm of bees are approaching.")