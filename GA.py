import matplotlib
import logging
import myLog
import numpy as np
import random

from Environment import Environment
from Rat import Rat
from Chrome import Chrome

class GA:
    """Gene Arithmetic"""
    def __init__(self, env, pop_size, max_gen, cross_rate, mutate_rate, select_press):
        self.env = env
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.select_press = select_press

        self.rat_list = []

    def Run(self):
        """execute function"""
        random.seed()
        self.Initialize(self.max_gen, self.env)
        # for i in range(self.max_gen):
        #     logging.INFO("------This is the %d generation------" % i)
        #     self.Crossover()
        #     self.Mutate()
        #     self.Elite_Select()

    def Display(self):
        """display function"""

    def Initialize(self, max_gen, env):
        logging.info("------GA Initialize begin------")
        for i in range(self.pop_size):
            self.rat_list.append(Rat(env))


    # def Crossover(self):
    #
    # def Mutate(self):
    #
    # def Elite_Select(self):
    #
    # def Test(self):