from species import *

class Simulator():

  steps = 0
  initial_population = 0
  repop_rate = 0.0
  death_rate = 0.0
  population = None

  def __init__(self, simulated_steps, init_pop, repop, death):
    """A Simulator utilizes species to simulate
       some action over a set of steps. Steps are
       an ambiguous time period that is not specified.

       :param int simulated_steps: The amount of steps to simulate
       :param int init_pop: The initial population size
       :param float repop: The repopulation probability of the simulated species
       :param float death: The death probability of the simulated species
    """

    self.steps = simulated_steps
    self.initial_population = init_pop
    self.repop_rate = repop
    self.death_rate = death
    self.population = [Species(self.repop_rate, self.death_rate)] * self.initial_population
    self.run()

  def step(self):
    """Performs a single step in the simulation"""
    
    newborns = []
    survivors = []
    deaths = []
    for specimen in self.population:
      reproduced, died = specimen.action()
      if reproduced and died:
        newborns.append(Species(self.repop_rate, self.death_rate))
        deaths.append(specimen)
      elif reproduced:
        newborns.append(Species(self.repop_rate, self.death_rate))
        survivors.append(specimen)
      elif died:
        deaths.append(specimen)
      else:
        survivors.append(specimen)
    
    death_count = len(deaths)
    newborn_count = len(newborns)
    self.population = survivors
    self.population = self.population + newborns

    return death_count, newborn_count

  def run(self):
    """Runs the simulation (basically the Matrix)"""

    print("Population:", len(self.population))
    print("Deaths: 0")
    print("Newborns: 0")
    print("----------Starting simulation----------")

    for i in range(self.steps):
      deaths, newborns = self.step()
      print("----------STEP {0}----------".format(i+1))
      print("Population:", len(self.population))
      print("Deaths this step:", deaths)
      print("Newborns this step:", newborns)


if __name__ == "__main__":
  steps = 50
  initial_population = 500
  repopulation_rate = 0.5
  death_rate = 0.5

  firstSim = Simulator(steps, initial_population, repopulation_rate, death_rate)

