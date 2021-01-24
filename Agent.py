from Building import *
import logging


class Agent:
    """工程师基类"""

    def __init__(self, name="Agent", start_depot=Depot()):
        self.name = name
        self.start_depot = start_depot
        self.position = Point2D(0, 0)

    def Copy(self):
        n_Agent = Agent()
        n_Agent.name = self.name
        n_Agent.start_depot = self.start_depot
        n_Agent.position = self.position
        return n_Agent

    def Display_log(self):
        logging.debug("---Agent Status---")
        logging.debug("Agent name:" + self.name + "\tAgent Position:" + self.position)


class GoodAgent(Agent):
    """好工程师类"""

    def __init__(self, name="GoodAgent", start_depot=Depot()):
        Agent.__init__(self, name, start_depot)
        self.velocity = 10
        self.com_max = 50
        self.travel_cost = 10
        self.repair_cost = 10
        self.com_num = self.com_max

    def Copy(self):
        n_Agent = GoodAgent()
        n_Agent.name = self.name
        n_Agent.start_depot = self.start_depot
        n_Agent.position = self.position
        n_Agent.velocity = self.velocity
        n_Agent.com_max = self.com_max
        n_Agent.travel_cost = self.travel_cost
        n_Agent.repair_cost = self.repair_cost
        n_Agent.com_num = self.com_num
        return n_Agent

    def Display_log(self):
        logging.debug("---Agent Status---")
        logging.debug("Agent name:" + self.name + "\tAgent Position:" + str(self.position))
        logging.debug("Now Component number: %d" % self.com_num)


class BadAgent(Agent):
    """坏工程师类"""

    def __init__(self, name="BadAgent", start_depot=Depot()):
        Agent.__init__(self, name, start_depot)
        self.velocity = 5
        self.com_max = 30
        self.travel_cost = 5    # per distance
        self.repair_cost = 5
        self.com_num = self.com_max

    def Copy(self):
        n_Agent = BadAgent()
        n_Agent.name = self.name
        n_Agent.start_depot = self.start_depot
        n_Agent.position = self.position
        n_Agent.velocity = self.velocity
        n_Agent.com_max = self.com_max
        n_Agent.travel_cost = self.travel_cost  # per distance
        n_Agent.repair_cost = self.repair_cost
        n_Agent.com_num = self.com_num
        return n_Agent

    def Display_log(self):
        logging.debug("---Agent Status---")
        logging.debug("Agent name:" + self.name + "\tAgent Position:" + str(self.position))
        logging.debug("Now Component number: %d" % self.com_num)