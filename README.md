# Escape of the Bees 🐝
- A text-based adventure game by Megan Brown
- Last Updated Readme: 4/19/23

## About the Project
I created a text-based adventure game as my final project for CS 5001 - Intensive Foundations of Computer Science at Northeastern University. The goal was to create something of my own that would allow me to demonstrate concepts from the class and learn new skills. 
- *Timeframe:* ~5 weeks to plan, code, test, and document
- *Dates:* March & April 2023
- *Role:* Software Engineer (on a team of 1, so I was also the game designer)
- *Project:* Text-based adventure game

Key aspects of the project include using Object-oriented Programming, fitting data types and structures, and Git for version control. For example, I created the dice and scenes as objects, and this allowed me to write more modular code that was easier to test and maintain. I used dictionaries to keep track of each player’s health score. Also, I learned Git during this timeframe, and I was able to use it for this project.

### About the Game
*Instructions:* To play the game, run the game.py file and interact with the text-based prompts.

*Story Premise:* You are driving to a trailhead with two of your close friends - Martin and Robin. All of a sudden, you are surrounded by a swarm of angry killer bees. Follow the story and roll the dice to find out how you navigate this situation.

## Retrospective
Through this project, I learned a lot about software development best practices. I was also better able to internalize these learnings, because I had experienced them in a hands-on way (learning by doing). 

I started the project by creating dice as a class, to begin with an object-oriented approach. This was easy to implement and test, making everything related to the dice and dice rolls go smoothly. On the flip-side, I implemented the game.py module, which contains most of the app logic, in a more procedural style, using variables to hold information about each scene. This made the game.py file hard to test, and made me realize I needed to refactor. 

While coming to this realization was disappointing (I wished I had known patterns of good design, so I could implement it well the first time), I was very glad that I had been learning and using Git this entire time. Because I was using Git, I was able to create another branch (called megan-oop_story_update) and use it to work on the refactoring needed to turn scenes into objects and make the game.py module more modular. Coding on this branch was a relief, because it made me unafraid to refactor most of my original software design. I knew that I could always fall back on my old code in the main branch, if I needed to show a working demo. Fortunately, the refactoring was successful, and I was able to demo the game running on the newly refactored code.

With more time, I would make the following improvements to this project: (1) separate the game’s strings from the app logic, and (2) code players as objects and save their health scores as an attribute. Separating the strings from the logic would allow for easier testing, localization, and the ability for someone who doesn’t know how to code to contribute to the game storyline. Coding players as objects would make the game easier to test, simplify app logic, and more easily allow for other interesting possibilities with the game design (such as updating this to be a turn-based, multiplayer game).

I want to continue to learn and practice patterns of good software design. This would help me plan better architecture from the beginning to reduce the need for refactoring and increase the software’s flexibility for new features. I’m also interested in learning how to implement telemetry data to get more visibility into the health of the program, and learn testing best practices. Continuing to be mindful of these goals while building out this project will likely help me progress, as well as taking CS 5004 - Object Oriented Design this summer.