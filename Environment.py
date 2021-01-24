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

        self.avg_cost = 0       #平均固定成本

    def Initialize(self):
        self.depot_list.append(Depot("Depot00", Point2D(10, 10)))
        self.depot_list.append(Depot("Depot01", Point2D(-10, -10)))

        self.factory_list.append(Factory("Factory00", Point2D(1, 0), 1, Point2D(1, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory01", Point2D(2, 0), 1, Point2D(2, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory02", Point2D(3, 0), 1, Point2D(3, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory03", Point2D(4, 0), 1, Point2D(4, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory04", Point2D(5, 0), 1, Point2D(5, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory05", Point2D(6, 0), 1, Point2D(6, 1), 1, 20, 10, 1))
        self.factory_list.append(Factory("Factory06", Point2D(7, 0), 1, Point2D(7, 1), 1, 20, 10, 1))

        self.agent_list.append(GoodAgent("Agent00", "Depot00"))
        self.agent_list.append(GoodAgent("Agent01", "Depot00"))
        self.agent_list.append(BadAgent("Agent02", "Depot00"))
        self.agent_list.append(GoodAgent("Agent03", "Depot01"))
        self.agent_list.append(BadAgent("Agent04", "Depot01"))

        self.depot_num = len(self.depot_list)
        self.factory_num = len(self.factory_list)
        self.agent_num = len(self.agent_list)

        self.avg_cost = self.Average_cost_calculation()

        logging.info("Environment Initialize Done!")

    def Average_cost_calculation(self):
        """计算平均固定成本"""
        cost_sum = 0
        for agent in self.agent_list:
            cost_sum += agent.repair_cost
        avg = cost_sum / self.agent_num
        return avg

    def displayEnvironment(self):
        print("------DISPLAY ENVIRONMENT INFO------")
        print("Depot number: %d\tFactory number: %d\t Agent number: %d\n" % (\
            self.depot_num, self.factory_num, self.agent_num))


