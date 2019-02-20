# On-Sets

On-Sets is a board game created in 1965 by Yale professor Layman Allen and produced by [The Accelerated Learning Foundation](http://www.gamesforthinkers.org/). This game is based on set theory, and teaches its players to create and describe sets of colored objects using Union, Intersection, Set Difference, Set Complement, the Universe, and the Null Set. The game's full rules can be found [here](http://agloa.org/wp-content/uploads/OSRules1617.pdf).

On-Sets is currently played by students in grades 4-12 through [AGLOA](http://agloa.org/) -- The Academic Games League of America. AGLOA is a non-profit organization that encourages academic competition, and works to develop “Thinking Kids” of character, excellence, and integrity. 

The goal of this project is to create a digital version of this game using Python and [PyGame](http://www.pygame.org/news). This is an in-progress project, so check back soon for updates!

## Motivation

From 2004 to 2009, I participated in Academic Games. For those five years I traveled to local, state, and national tournaments competing on my school's team. During that time, I made many invaluable connections to other students who were passionate about learning and growth through competition. My coach was one of my biggest influences while growing up, and the lessons we learned through him will be carried with us throughout our entire lives. I also began to love competing; in 2008 I won both the Junior of Year award and 4th place in Equations (another game that I plan on getting to) at the AGLOA National Tournament. These games are an integral part of my life; through them I met amazing people, learned important life lessons, and gained a passion for competition.

While teaching myself Python, I decided that I needed a project to motivate me, and help reinforce the concepts that I was learning. I thought recreating one of my favorite games would be a great way to learn the fundamentals of Python and version control through Git. Through this project, I hope to learn about the following concepts:

* Fundamentals of programming
* Python and PyGame
* Abstract Syntax Trees
* Algorithms
* AI in gaming
* Version control

## What's Inside
The On-Sets directory contains:
  * `os_expression_eval.py`: All AST objects (Lexer, Parser, and the Interpreter)
  * `OnSets.py`: Basic game assets and GUI elements (coming soon)
  
## Tasks
- [x] Create basic structure for game assets (e.g. cubes, cards, operators)
  - [x] Make lists of game's assets grouped by their category
  - [x] Create a function to simulate a generic six-sided cube being rolled
  - [x] Add a function for generating a Universe, the size of which is chosen by the user
 
- [ ] Solution evaluator, implement through an AST
  - [x] Lexer/Tokenizer
  - [x] Parser
  - [ ] Interpreter

- [ ] Gameplay
  - [ ] Game setup
  - [ ] Player turns
  - [ ] End game and scoring
  - [ ] Variatons and division rule adjustments

- [ ] GUI
  - [ ] The board
  - [ ] The assets (cubes, cards, timer, challenge cube)
  - [ ] I/O and asset interactions

- [ ] Extras
  - [ ] AI controlled player with different difficulty levels
  - [ ] Challenges (e.g. have the user win in a set number of turns under certain conditions)
 
 ## Running It
 
 Coming soon!
