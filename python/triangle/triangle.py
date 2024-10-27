def is_triangle(sides):
    return all(side > 0 for side in sides) and sum(sides) > 2 * max(sides)

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
