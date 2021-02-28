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
        self.depot_list.append(Depot("Depot00", Point2D(100, 100)))
        self.depot_list.append(Depot("Depot01", Point2D(-100, -100)))
        self.depot_list.append(Depot("Depot02", Point2D(-100, 100)))

        self.factory_list.append(Factory("Factory00", Point2D(15, 3), 1, Point2D(-1, 1), 5, 20, 15, 1))
        self.factory_list.append(Factory("Factory01", Point2D(-62, 90), 1, Point2D(2, 1), 5, 20, 30, 1))
        self.factory_list.append(Factory("Factory02", Point2D(3, 67), 1, Point2D(-3, -1), 5, 20, 0, 1))
        self.factory_list.append(Factory("Factory03", Point2D(44, 24), 1, Point2D(4, 11), 5, 20, 50, 1))
        self.factory_list.append(Factory("Factory04", Point2D(5, 34), 2, Point2D(15, -13), 5, 15, 20, 1))
        self.factory_list.append(Factory("Factory05", Point2D(-40, 10), 2, Point2D(6, -12), 5, 15, 5, 1))
        self.factory_list.append(Factory("Factory06", Point2D(-10, -50), 3, Point2D(-7, 31), 5, 15, 40, 1))
        self.factory_list.append(Factory("Factory07", Point2D(84, 24), 1, Point2D(-4, 11), 5, 20, 50, 1))
        self.factory_list.append(Factory("Factory08", Point2D(52, 34), 2, Point2D(5, -13), 5, 15, 20, 1))
        self.factory_list.append(Factory("Factory09", Point2D(-40, 0), 2, Point2D(6, -2), 5, 15, 5, 1))
        self.factory_list.append(Factory("Factory10", Point2D(-10, -5), 3, Point2D(-7, 131), 5, 15, 40, 1))

        self.agent_list.append(GoodAgent("Agent00", "Depot00"))
        self.agent_list.append(GoodAgent("Agent01", "Depot02"))
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


