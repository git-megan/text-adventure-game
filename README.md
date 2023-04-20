# Escape of the Bees 🐝
- A text-based adventure game by Megan Brown
- Last Updated Readme: 20 April 2023

## About the Game
*Story Premise:* You are driving to a trailhead with two of your close friends - Martin and Robin. All of a sudden, you are surrounded by a swarm of angry killer bees. Follow the story and roll the dice to find out how you navigate this situation.

*How to Play:* If you have Python on your computer, download the files and run game.py. Interact with the text-based prompts.

## About the Project
I created a text-based adventure game as my final project for CS 5001 - Intensive Foundations of Computer Science at Northeastern University. The goal was to create something of my own that would allow me to demonstrate concepts from the class and learn new skills. 
- *Timeframe:* ~5 weeks to plan, code, test, and document
- *Dates:* March & April 2023
- *Role:* Software Engineer (on a team of 1, so I was also the game designer)
- *Project:* Text-based adventure game

### The Challenge
I decided to use this project as an opportunity to get more practice with object-oriented programming and using fitting data types and structures. I also set the goal of learning the basics of Git for version control, so that I could set myself up to contribute to team projects in the future.

### The Process
1. *Planning & Feedback:* I wrote a spec to plan the game requirements and my approach to coding the game. The spec also allowed me to scope the project for the 5-week timeframe. I then got feedback from Professor Mark Miller about the scope and how I'd demonstrate concepts from CS 5001 (i.e. objects, dictionaries, etc.).
2. *Creating a V1:* I learned Git and used it while developing the first version of this game. I implemented dice as objects, which was easy to plan and test. I then implemented a tracker for health scores using a dictionary, and I put most of the strings for the game in storyline.py file. While the dice class was easy to test and use, I realized that game.py (which contains most of the game logic) needed to be more modular and easier to test.
3. *Scenes as Objects:* I created a branch so that I could do a major refactoring of game logic. I decided to implement scenes (i.e. a segment in the game in which there is a scenario, a dice roll, and a revealing of the outcome) as objects. After developing and testing this update, I merged the branch with main (just in time for a live demo).
4. *Demo Day:* On 17 April 2023, I presented the project, demoed the game using the latest version in which scenes are objects, and walked through the code. The demo went well, and I received feedback about how to continue improving the codebase.

### The Impact
Through this project, I got a better understanding of how to write more modular, flexible, object-oriented code. I also practiced good development habits such as planning, testing, and documentation. Additionally, I learned the basics of how to use Git & GitHub.

### Development Notes
While the game can be played, it is still a work in progress. I plan to make the following improvements:
| *Update* | *Purpose* | *Estimated Worklaod* |
| --- | --- | ---|
| Strings in Text File | Separate strings from app logic | L |
| Players as Objects | Improve upon current OOP design, implement health score as attribute | M |
| Host Game Online | Allow for people to play the game through a website, rather than download the game files and Python | M |

## Retrospective
Through this project, I learned a lot about software development best practices. I was also better able to internalize these learnings, because I had experienced them in a hands-on way (learning by doing). 

I started the project by creating dice as a class, to begin with an object-oriented approach. This was easy to implement and test, making everything related to the dice and dice rolls go smoothly. On the flip-side, I implemented the game.py module, which contains most of the app logic, in a more procedural style, using variables to hold information about each scene. This made the game.py file hard to test, and made me realize I needed to refactor. 

While coming to this realization was disappointing (I wished I had known patterns of good design, so I could implement it well the first time), I was very glad that I had been learning and using Git this entire time. Because I was using Git, I was able to create another branch (called megan-oop_story_update) and use it to work on the refactoring needed to turn scenes into objects and make the game.py module more modular. Coding on this branch was a relief, because it made me unafraid to refactor most of my original software design. I knew that I could always fall back on my old code in the main branch, if I needed to show a working demo. Fortunately, the refactoring was successful, and I was able to demo the game running on the newly refactored code.

With more time, I would make the following improvements to this project: (1) separate the game’s strings from the app logic, and (2) code players as objects and save their health scores as an attribute. Separating the strings from the logic would allow for easier testing, localization, and the ability for someone who doesn’t know how to code to contribute to the game storyline. Coding players as objects would make the game easier to test, simplify app logic, and more easily allow for other interesting possibilities with the game design (such as updating this to be a turn-based, multiplayer game).

I want to continue to learn and practice patterns of good software design. This would help me plan better architecture from the beginning to reduce the need for refactoring and increase the software’s flexibility for new features. I’m also interested in learning how to implement telemetry data to get more visibility into the health of the program, and learn testing best practices. Continuing to be mindful of these goals while building out this project will likely help me progress, as well as taking CS 5004 - Object Oriented Design this summer.