"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    Example:
    >>> bake_time_remaining(20)
    20
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calculate the total preparation time for the lasagna.

    This function calculates the total preparation time required for the lasagna,
    based on the number of layers. The preparation time per layer is defined by
    the `PREPARATION_TIME` constant.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - the total preparation time in minutes.

    Example:
    >>> preparation_time_in_minutes(3)
    6
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate the total elapsed time for preparing and baking the lasagna.

    This function calculates the total elapsed time required for preparing and baking
    the lasagna, based on the number of layers and the elapsed bake time. It uses
    the `bake_time_remaining` and `preparation_time_in_minutes` functions to determine
    the total time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - the total elapsed time in minutes.

    Example:
    >>> elapsed_time_in_minutes(3, 20)
    26
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)