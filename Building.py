import logging

from Point2D import Point2D


class Building:
    """所有地点的基类"""
    buildingCount = 0

    def __init__(self, name="Building", position=Point2D(0, 0)):
        self.name = name
        self.position = position
        Building.buildingCount += 1

    def __str__(self):
        return self.name

    def displayCount(self):
        logging.debug("Total Building Count: %d" % Building.buildingCount)

    def displayBuilding(self, time):
        logging.debug("Name: " + self.name + ", Position: " + str(self.position))


# testbuilding = Building('Factory', Point2D(1,1))
# testbuilding.displayBuilding()

class Depot(Building):
    """车场类"""

    def __init__(self, name="Depot", position=Point2D(0, 0)):
        Building.__init__(self, name, position)
        self.recharge_duration = 10


class Factory(Building):
    """可移动工厂类"""

    def __init__(self, name="Factory", position=Point2D(0, 0), velocity=0, direction=Point2D(0, 0), \
                 rep_duration=0, com_need=0, bro_time=0, punish_factor=1):
        Building.__init__(self, name, position)
        self.velocity = velocity
        self.direction = direction
        self.rep_duration = rep_duration
        self.com_need = com_need
        self.bro_time = bro_time
        self.punish_factor = punish_factor
        self.direction_normalization()

    def Get_position(self, time):
        m_position = Point2D(0, 0)
        m_position = self.position + m_position
        m_position.x = m_position.x + self.direction.x * time
        m_position.y = m_position.y + self.direction.y * time
        return m_position

    def direction_normalization(self):
        self.direction.normalization()

    def displayBuilding(self, time):
        logging.debug("Name: " + self.name + ", Position: " + str(self.Get_position(time)))
