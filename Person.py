import random
from Virus import Virus


class Person:
    ''' The simulation will contain people who will make up a population.'''

    def __init__(self, is_vaccinated, infection=None):
        ''' We start out with is_alive = True
        All other values will be set by the simulation through the parameters when it instantiates each Person object.
        '''
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # virus object

    def did_survive_infection(self):
        ''' Generate a random number between 0.0 and 1.0 and compare to the virus's mortality_num.
        If the random number is smaller, person dies from the disease. Set the person's is alive attribute to False
        If Person survives, they become vaccinated and they have no infection (set the vaccinated attribute to True and the infection to None)
        Return True if they survived the infection and False if they did not. 
        '''

        survival_chance = random.uniform(0, 1)

        if self.infection.mortality_num < survival_chance:
            self.is_alive = False
            return False
        elif self.infection.mortality_num > survival_chance:
            self.is_vaccinated = True
            self.infection = None
            return True
