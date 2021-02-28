import numpy
import logging
import random
import math
from Building import *


class Chrome:
    chromeCount = 0

    def __init__(self, agent_number):
        self.name = "GENE" + str(Chrome.chromeCount)

        self.agent_number = agent_number
        self.cost = 0
        self.work_duration = 0
        self.travel_distance = 0

        self.path = []
        self.gene_list = []
        self.meet_position = []

        Chrome.chromeCount += 1

    def init_check(self, agent, factory, env):
        """检查但不插入"""
        return True

    def cross_check(self, agent, factory, index, env):
        """检查但不插入"""
        return True

    def Copy(self):
        n_Chrome = Chrome(self.agent_number)
        for gene in self.gene_list:
            n_Chrome.gene_list.append(gene)
        for position in self.meet_position:
            n_Chrome.meet_position.append(position)
        n_Chrome.cost = self.cost
        n_Chrome.work_duration = self.work_duration
        n_Chrome.travel_distance = self.travel_distance
        n_Chrome.path = self.path
        return n_Chrome

    def Delete_redundant_element(self, compare_list):
        logging.debug("Before Delete, Gene_list: " + str(self.gene_list))
        n_gene_list = [x for x in self.gene_list if x not in compare_list]
        self.gene_list = n_gene_list
        logging.debug("After Delete, Gene_list: " + str(self.gene_list))

    def Mutate(self, mutate_list, mutate_rate):
        for gene in self.gene_list:
            if random.random() < mutate_rate:
                logging.debug("Gene %d will mutate. It has been put into Mutation Box" % gene)
                mutate_list.append(gene)
                self.gene_list.remove(gene)
                logging.debug("Mutation Box:" + str(mutate_list))

    def Cost_calculation(self, env):
        """更新+返回"""
        logging.debug("Agent 0%d cost calculation begin." % self.agent_number)
        self.cost = 0
        self.travel_distance = 0
        self.work_duration = 0
        self.path = []
        self.meet_position = []

        agent = env.agent_list[self.agent_number].Copy()
        plan = []  # 实体形式
        ad_plan = []  # 实体形式
        for gene in self.gene_list:
            plan.append(env.factory_list[gene])

        for i in range(len(plan)):
            target = plan[i]
            logging.debug("---Processing Target %d---" % i)
            target.displayBuilding(self.work_duration)

            if agent.com_num < target.com_need:  # 零件不足，需返场补充
                target = self.Find_depot(env, agent)
                ad_plan.append(target)
                logging.debug("Components insufficient, Agent 0%d will go to " % self.agent_number + target.name + \
                              "to recharge.")
                self.Plan_display(ad_plan)
                self.Cost_update(agent, target)


            target = plan[i]  # 零件充足，继续维修
            ad_plan.append(target)
            logging.debug("Components sufficient, Agent 0%d will go to " % self.agent_number + target.name)
            self.Plan_display(ad_plan)
            self.Cost_update(agent, target)

        final_depot = self.Find_depot(env, agent)   #任务结束，返场休息
        ad_plan.append(final_depot)
        logging.debug("ALL work DONE, Agent 0%d will go to " % self.agent_number + final_depot.name + \
                      "to REST.")
        self.Plan_display(ad_plan)
        self.Cost_update(agent, final_depot, True)

        self.path = ad_plan
        del agent
        return self.cost

    def Cost_update(self, agent, target, final_flag=False):
        logging.debug("---Cost Update---")
        if isinstance(target, Depot):   #目标为车场类型
            self.meet_position.append(target.position)
            self.travel_distance += abs(agent.position - target.position)
            self.work_duration += (abs(agent.position - target.position) / agent.velocity)
            self.cost += self.travel_distance * agent.travel_cost
            agent.position = target.position
            if not final_flag:
                self.work_duration += target.recharge_duration
                agent.com_num = agent.com_max
                logging.debug("Recharge DONE\n---After recharge---")
                agent.Display_log()
                return
            logging.debug("---REST---(Agent 0%d)" % self.agent_number)
            agent.Display_log()
        else:   #目标为工厂
            # Travel
            travel_duration = self.Travel_duration_calculation(agent, target)
            self.work_duration += travel_duration
            self.travel_distance += (travel_duration * agent.velocity)
            self.cost += (travel_duration * agent.velocity * agent.travel_cost)
            agent.position = target.Get_position(self.work_duration)
            self.meet_position.append(agent.position)
            logging.debug("MEET POSITION APPEND:" + str(agent.position))
            # Repair
            agent.com_num -= target.com_need
            self.cost += (agent.repair_cost + abs(self.work_duration - target.bro_time) * target.punish_factor) # 立即维护，惩罚成本
            self.work_duration += target.rep_duration
            agent.position = target.Get_position(self.work_duration)
            logging.debug(target.name +" has been repaired!\tNow cost: %f\tNow working duration: %f" % (self.cost, self.work_duration))

    def Travel_duration_calculation(self, agent, target):
        relative_vector = target.Get_position(self.work_duration) - agent.position
        relative_vector.normalization()
        a = 1
        b = 2 * target.velocity * target.direction.x * relative_vector.x + 2 * target.velocity * target.direction.y * relative_vector.y
        c = target.velocity ** 2 - agent.velocity ** 2
        delta = b ** 2 - 4 * c
        if delta < 0:
            logging.error("No feasible solve! DELTA < 0")
            exit()
        x = (-b + math.sqrt(delta)) / (2 * a)
        if x < 0:
            logging.error("No feasible solve! solve < 0")
            exit()
        if x == 0:
            return 0
        travel_duration = abs(relative_vector) / x
        return travel_duration


    def Find_depot(self, env, agent):
        """返回最近的车场"""
        min_distance = abs(agent.position - env.depot_list[0].position)
        target = env.depot_list[0]
        for depot in env.depot_list:
            if abs(agent.position - depot.position) < min_distance:
                min_distance = abs(agent.position - depot.position)
                target = depot
        return target

    def Plan_display(self, plan):
        name_list = []
        for building in plan:
            name_list.append(str(building))
        logging.debug("Plan:\t" + str(name_list))

    def Display(self):
        print("Agent: 0" + str(self.agent_number) + "\t" + str(self.gene_list))

    def Display_log(self):
        logging.debug("Agent: 0" + str(self.agent_number) + "\t" + str(self.gene_list))
