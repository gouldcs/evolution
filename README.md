# Evolution
## A Simulated Model of Basic Population Growth
### Author: Cameron G. Gould, December 2020
This is a simple Python program that creates a simulation containing a population of
a single Species. The population grows and shrinks based on the Species' probability of death and/or repopulation.

The structure of the program is very basic. There is a simulator class, and a species class. The species has two actions: mate, and die. Simple enough. The Simulator runs in a specified amount of steps. During each step, a specimen can either mate, die, both, or neither. By default, the probabilities (found in `__main__` within `simulator.py`) for dying and mating are set to `0.5` (50% chance of each). You can modify this and play with the values all you want.

I plan to add basic graphing and also modify the structure of the simulator such that multiple types of species can be added to a single simulation.

## Running the simulation
Running the simulation is as barebones as it gets. I developed this using Pyhon 3.8.6, though any version of Python 3 should work (I will not be supporting Python 2).

1. open terminal, and make your way to .../evolution/src
2. run `python3 simulator.py`

Congratulations. You did it! 