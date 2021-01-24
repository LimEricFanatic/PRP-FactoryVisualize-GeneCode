import matplotlib
import logging
import myLog
import numpy as np
import random
import time
import matplotlib.pyplot as plt

from tqdm import tqdm
from tqdm._tqdm import trange

from Environment import Environment
from Rat import Rat
from Chrome import Chrome


class GASA:
    """Gene Arithmetic"""

    def __init__(self, env, pop_size, max_gen, cross_rate, mutate_rate, T_max, T_min, SA_rate):
        self.env = env
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.T_max = T_max
        self.T_min = T_min
        self.SA_rate = SA_rate

        self.rat_list = []
        self.rat_best = Rat(self.env)
        self.best_cost_list = []

    def Run(self):
        """execute function"""
        random.seed()
        self.Initialize(self.max_gen, self.env)
        for i in trange(self.max_gen):
            time.sleep(0.01)
            # logging.info("\n------This is the %d generation------" % i)
            self.Crossover_and_Mutation()
            self.Select()
            self.Elite_select()
            self.rat_best.BestRatDisplay_log()

    def Display(self):
        """display function"""
        print("POP SIZE: %d" % (len(self.rat_list)))
        print("---Best Rat---")
        self.rat_best.Display()
        self.rat_best.Display_log()

        # Pyplot制图
        x = np.arange(1, self.max_gen+1)
        y = self.best_cost_list
        plt.title("GA Best Fitness Curve")
        plt.plot(x, y)
        plt.show()

    def Initialize(self, max_gen, env):
        # logging.info("------Initialize begin------")
        for i in range(self.pop_size):
            rat = Rat(env)
            rat.Initialize(self.env.depot_num, self.env.factory_num, self.env.agent_num, self.env)
            self.rat_list.append(rat)

    def Crossover_and_Mutation(self):
        logging.debug("------Crossover and Mutate begin------")
        rat_num = len(self.rat_list)
        for i in range(rat_num):
            for j in range(i + 1, rat_num):
                if random.random() < self.cross_rate:
                    logging.debug("Total Rat is %d\tRatA index %d\tRatB index %d" % (len(self.rat_list), i, j))
                    # GASA START
                    T = self.T_max
                    logging.debug("Temperature MAX\t now %f" % T)
                    while T >= self.T_min:
                        ratA, ratB = self.Crossover(self.rat_list[i], self.rat_list[j], T)
                        m_ratA, m_ratB = self.Mutate(ratA, ratB, T)
                        T *= self.SA_rate
                        logging.debug("Now Temperature is %f" % T)
                    self.rat_list.append(m_ratA)
                    self.rat_list.append(m_ratB)
                    logging.debug("---After SA, RAT info---")
                    m_ratA.Display_log()
                    m_ratB.Display_log()
                    logging.debug("Temperature < T_min, SA END")

    def Crossover(self, rat_A, rat_B, T):
        """对A，B个体进行操作，注意要改变个体本身，要产生新个体"""
        logging.debug("---Crossover Begin---(%s, %s)" % (rat_A.name, rat_B.name))
        chrome_number = random.choice(range(self.env.agent_num))
        logging.debug("crossover number is: %d" % chrome_number)
        n_rat_A = rat_A.Copy()
        n_rat_B = rat_B.Copy()
        a = n_rat_A.chrome_list[chrome_number]
        b = n_rat_B.chrome_list[chrome_number]
        a.Display_log()
        b.Display_log()
        if len(a.gene_list) == 0 and len(b.gene_list) == 0:
            logging.debug("No gene exist in these chromes, RETRY!")
            return self.Crossover(n_rat_A, n_rat_B, T)
        F_ab = [x for x in a.gene_list if x in b.gene_list]
        F_a = [y for y in a.gene_list if y not in F_ab]
        F_b = [z for z in b.gene_list if z not in F_ab]
        logging.debug("F_ab:" + str(F_ab) + "\tF_a:" + str(F_a) + "\tF_b:" + str(F_b))

        logging.debug("Before Duplicate, rat num is: %d, following is RatA, RatB" % len(self.rat_list))
        rat_A.Display_log()
        rat_B.Display_log()

        # self.rat_list.append(n_rat_A)
        # self.rat_list.append(n_rat_B)
        logging.debug("After Duplicate, rat num is: %d" % len(self.rat_list))

        logging.debug("---Before Switch--- (A,B)")
        n_rat_A.chrome_list[chrome_number].Display_log()
        n_rat_B.chrome_list[chrome_number].Display_log()
        tmp = a.Copy()
        n_rat_A.chrome_list[chrome_number] = n_rat_B.chrome_list[chrome_number].Copy()
        n_rat_B.chrome_list[chrome_number] = tmp
        logging.debug("---After Switch--- (A,B)")
        n_rat_A.chrome_list[chrome_number].Display_log()
        n_rat_B.chrome_list[chrome_number].Display_log()

        n_rat_A.Delete_redundant_element(F_b, chrome_number)
        n_rat_B.Delete_redundant_element(F_a, chrome_number)

        n_rat_A.Insert_element(F_a)
        n_rat_B.Insert_element(F_b)

        logging.debug("RatA, RatB, newRatA, newRatB")
        rat_A.Display_log()
        rat_B.Display_log()
        n_rat_A.Display_log()
        n_rat_B.Display_log()

        new_rat_1 = self.SA_deal(rat_A, n_rat_A, T)
        new_rat_2 = self.SA_deal(rat_B, n_rat_B, T)

        return new_rat_1, new_rat_2

    def Mutate(self, ratA, ratB, T):
        logging.debug("------RAT Mutate Begin------(%s, %s)" % (ratA.name, ratB.name))
        n_ratA = ratA.Copy()
        n_ratB = ratB.Copy()
        n_ratA.Mutate(self.mutate_rate)
        n_ratB.Mutate(self.mutate_rate)
        new_rat_A = self.SA_deal(ratA, n_ratA, T)
        new_rat_B = self.SA_deal(ratB, n_ratB, T)
        return  new_rat_A, new_rat_B

    def Select(self):
        if len(self.rat_list) == 0:
            logging.error("No rat survive!")
            exit()
        for rat in self.rat_list:
            rat.Fitness_calculation()
        pop_fitness_max = self.rat_list[0].fitness
        pop_fitness_min = self.rat_list[0].fitness
        for rat in self.rat_list:
            if rat.fitness > pop_fitness_max:
                pop_fitness_max = rat.fitness
                break
            if rat.fitness < pop_fitness_min:
                pop_fitness_min = rat.fitness
                break

        relative_fitness_sum = 0
        for rat in self.rat_list:
            tmp = rat.Relative_fitness_calculation(pop_fitness_max, pop_fitness_min, self.env.avg_cost)
            relative_fitness_sum += tmp

        prob_sum = 0
        for rat in self.rat_list:
            prob_sum += rat.relative_fitness
            rat.accumulation_probability = prob_sum / relative_fitness_sum

        n_rat_list = []
        for i in range(self.pop_size):
            select_prob = random.random()
            logging.debug("select_prob is %f" % select_prob)
            for j in range(len(self.rat_list)):
                if self.rat_list[j-1].accumulation_probability < select_prob <= self.rat_list[j].accumulation_probability:
                    logging.debug("The %d Rat is selected. It's accumulation_probability is %f, Former one is %f" % (
                        j, self.rat_list[j].accumulation_probability, self.rat_list[j-1].accumulation_probability))
                    n_rat_list.append(self.rat_list[j])
                    logging.debug("New Rat List has %d members." % len(n_rat_list))
                    break
        self.rat_list = n_rat_list

    def Elite_select(self):
        best_index = 0
        worst_index = 0
        logging.debug("Before Elite select, Survive Rat Num: %d" % len(self.rat_list))
        pop_fitness_min = self.rat_list[0].fitness
        pop_fitness_max = self.rat_list[0].fitness
        for i in range(len(self.rat_list)):
            if self.rat_list[i].fitness < pop_fitness_min:
                pop_fitness_min = self.rat_list[i].fitness
                best_index = i
                break
            if self.rat_list[i].fitness > pop_fitness_max:
                pop_fitness_max = self.rat_list[i].fitness
                worst_index = i
                break
        logging.debug("The best index %d\tCost is: %f\nThe worst index %d\tCost is: %f" % (\
            best_index, self.rat_list[best_index].fitness, worst_index, self.rat_list[worst_index].fitness))
        logging.debug("Before replace, rat num is %d" % len(self.rat_list))
        self.rat_best = self.rat_list[best_index].Copy()
        del self.rat_list[worst_index]
        logging.debug("After Delete, rat num is %d" % len(self.rat_list))
        self.rat_list.append(self.rat_best)
        self.best_cost_list.append(self.rat_best.fitness)
        logging.debug("After replace, rat num is %d" % len(self.rat_list))

    def SA_deal(self, parent_rat, son_rat, T):
        logging.debug("SA_deal. Parent: %s\t Son: %s" % (parent_rat.name, son_rat.name))
        parent_rat.Fitness_calculation()
        son_rat.Fitness_calculation()
        delta = parent_rat.fitness - son_rat.fitness
        if delta > 0:
            logging.debug("Delta > 0, Replace!")
            return son_rat
        else:
            logging.debug("Delta < 0, Prob!")
            prob = np.exp(delta / T)
            if prob > random.random():
                logging.debug("Prob YES, Replace!")
                return son_rat
            else:
                logging.debug("Prob NO, Reserve!")
                return parent_rat


    # def Test(self):
