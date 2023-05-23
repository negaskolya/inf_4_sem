# Dota 3 
Simple RPG game wrote on python using pygame
## Description
### Game control 
```WASD``` - move
```SPACE``` - shoot
```1,2,3,4``` - change gun, drink potions
## Modules 
* ```Main.py``` - general file which describes main cycle, rendering, etc.
* ```Constants.py``` - file with constants used in each modules.
* ```Textures.py``` - file which contains definitions of all textures used in game.
* ```Creatures.py``` - file which describes all creatures (Player, Demon).
* ```Projective.py``` - file which describes all damaging and flying
objects(arrows, fireballs, etc.)
* ```Menu.py``` - file that describes the menu.
* ```Barrier.py``` - file which describes solid objects(Barriers, Walls, Trees)
* ```Level.py``` - file which determine level enviroment and describes all
level activity
* ```Ai.py``` - file that is responsible for BFS algorithm to search shortest path from npc to player

## Requirements
Game requires the following to run:
* [Python](https://www.python.org/downloads/) 3.9.7
* [Pygame](https://www.pygame.org/wiki/about) 2.1.0
* You may also need [Tkinter](https://docs.python.org/3/library/tkinter.html) 8.6

## Usage
Starting via ```Main.py```:
```bash
python3 Main.py
````
## Authors
* [Aslan Taibov](https://github.com/aslanchek)

* [Philipp Polyakov](https://github.com/p6h6i6l)
