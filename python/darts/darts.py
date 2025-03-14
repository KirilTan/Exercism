import math

def score(x: float, y: float) -> int:
    distance = math.sqrt(x ** 2 + y ** 2)

    if distance <= 1:
        return 10  # Inner circle
    elif distance <= 5:
        return 5  # Middle circle
    elif distance <= 10:
        return 1  # Outer circle
    else:
        return 0  # Outside the target