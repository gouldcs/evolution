import random

class Species():
  mating_probability = 0.0
  death_probability = 0.0
  dead = False
  reproduced = False

  def __init__(self, mp, dp):
    """A Species represents a collection of specimen with
       specific mating and death probabilities as attributes.
       
       :param float mp: The mating probability
       :param float dp: The death probability
    """
    self.mating_probability = mp
    self.death_probability = dp
  
  def action(self):
    """A specimen takes a given action based on the given
       probabilities of that action. In this model, mating
       and death can BOTH happen to a specimen in a single
       step.
    """
    outcome = random.random()
    outcome2 = random.random()
    self.dead = True if outcome < self.death_probability else False
    self.reproduced = True if outcome2 < self.mating_probability else False

    return self.reproduced, self.dead
