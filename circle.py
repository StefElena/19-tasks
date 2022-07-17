from math import pi


def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("радиус имеет неправильное выражение")
    if radius < 0:
        raise ValueError("радиус имеет отрицательное значение")
    return pi * radius ** 2
