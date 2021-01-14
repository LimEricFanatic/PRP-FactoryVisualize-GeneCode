class Agent:
    """工程师基类"""

    def __init__(self, name, start_depot):
        self.name = name
        self.start_depot = start_depot


class GoodAgent(Agent):
    """好工程师类"""

    def __init__(self, name, start_depot):
        Agent.__init__(name, start_depot)
        self.velocity = 10
        self.com_max = 50
        self.travel_cost = 10
        self.repair_cost = 10


class BadAgent(Agent):
    """坏工程师类"""

    def __init__(self, name, start_depot):
        Agent.__init__(name, start_depot)
        self.velocity = 5
        self.com_max = 30
        self.travel_cost = 5
        self.repair_cost = 5
