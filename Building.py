from Point2D import Point2D


class Building:
    """所有地点的基类"""
    buildingCount = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Building.buildingCount += 1

    def displayCount(self):
        print("Total Building Count: %d" % Building.buildingCount)

    def displayBuilding(self):
        print("Name: ", self.name, ", Position: ", self.position, \
              ", Movable? ", self.movable)


# testbuilding = Building('Factory', Point2D(1,1), True)
# testbuilding.displayBuilding()

class Depot(Building):
    """车场类"""

    def __init__(self, name, position):
        Building.__init__(self, name, position)


class Factory(Building):
    """可移动工厂类"""

    def __init__(self, name, position, velocity, direction, rep_duration, com_need, bro_time):
        Building.__init__(self, name, position)
        self.velocity = velocity
        self.direction = direction
        self.rep_duration = rep_duration
        self.com_need = com_need
        self.bro_time = bro_time

        self.direction_normalization()

    def get_position(self, time):
        m_position = Point2D(0, 0)
        m_position.x = self.position + m_position
        m_position.x = m_position.x + self.direction.x * time
        m_position.y = m_position.y + self.direction.y * time
        return m_position

    def direction_normalization(self):
        self.direction.normalization()