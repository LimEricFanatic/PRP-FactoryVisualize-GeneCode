import numpy
import random
import logging

class Rat:
    ratCount = 0

    def __init__(self, env):
        self.name = "RAT" + Rat.ratCount
        self.chrome_list = []
        self.env = env
        self.Initialize(self.env.depot_num, self.env.factory_num, self.env.agent_num, self.env)
        Rat.ratCount += 1

    def Initialize(self, depot_num, factory_num, agent_num, env):
        init_agent_list = list(range(0, agent_num))
        init_factory_list = list(range(0, factory_num))
        print(init_factory_list)
        random.shuffle(init_factory_list)
        logging.debug("init allocate start!")
        while len(init_factory_list) != 0:
            test_factory = init_factory_list[0]
            test_agent = random.choice(init_agent_list)
            if self.init_check(test_agent, test_factory, env):
                self.init_allocate(test_agent, test_factory, env)
                del init_factory_list[0]
                logging.debug("Factory 0%d has been allocated to Agent 0%d." % (test_factory, test_agent))

    # def init_check(self, agent, factory, env):
    #
    # def init_allocate(self, agent, factory, env):
