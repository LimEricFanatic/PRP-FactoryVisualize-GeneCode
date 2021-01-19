from Building import *
from Agent import *
from Point2D import *

import logging


class Environment:
    def __init__(self):
        self.depot_list = []
        self.factory_list = []
        self.agent_list = []
        self.depot_num = 0
        self.factory_num = 0
        self.agent_num = 0

    def Initialize(self):
        self.depot_list.append(Depot("Depot00", Point2D(10, 10)))
        self.depot_list.append(Depot("Depot01", Point2D(-10, -10)))

        self.factory_list.append(Factory("Factory00", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory01", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory02", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory03", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory04", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory05", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))
        self.factory_list.append(Factory("Factory06", Point2D(0, 0), 1, Point2D(1, 1), 1, 10, 10))

        self.agent_list.append(GoodAgent("Agent00", "Depot00"))
        self.agent_list.append(GoodAgent("Agent01", "Depot00"))
        self.agent_list.append(BadAgent("Agent02", "Depot00"))
        self.agent_list.append(GoodAgent("Agent03", "Depot01"))
        self.agent_list.append(BadAgent("Agent04", "Depot01"))

        self.depot_num = len(self.depot_list)
        self.factory_num = len(self.factory_list)
        self.agent_num = len(self.agent_list)

        logging.info("Environment Initialize Done!")

    def displayEnvironment(self):
        print("------DISPLAY ENVIRONMENT INFO------\n")
        print("Depot number: %d\tFactory number: %d\t Agent number: %d" % (\
            self.depot_num, self.factory_num, self.agent_num))


