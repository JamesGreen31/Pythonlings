import math 
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        # TODO: return the distance from (x, y) to (0, 0)
        # Distance = Square Root of (x^2 + y^2). You can use "n ** 2" to raise a number to the second power
        return math.sqrt(self.x ** 2 + self.y ** 2)
