import numbers
import math


class GeoUtil:
    @staticmethod
    def degree2radius(degree):
        return degree * (math.pi / 180)
