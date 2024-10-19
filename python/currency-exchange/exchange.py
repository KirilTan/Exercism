"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    Calculates the exchanged value of a given budget in foreign currency using the provided exchange rate.

    :param:
        budget: float - The amount of money you are planning to exchange. This value should be a positive number.
        exchange_rate: float - The unit value of the foreign currency. This value should be a positive number.
    :return:
        float - The exchanged value of the foreign currency you can receive. The result is calculated by dividing the budget by the exchange rate.

    Example:
    >>> exchange_money(127.5, 1.2)
    106.25
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """
    Calculates the remaining amount of the original currency after exchanging a specified amount.

    :param:
        budget: float - The total amount of money you initially have. This value should be a positive number.
        exchanging_value: float - The amount of money you plan to exchange. This value should be a positive number and less than or equal to the budget.
    :return:
        float - The remaining amount of your original currency after the exchange. The result is calculated by subtracting the exchanging value from the budget.

    Example:
    >>> get_change(127.5, 120)
    7.5
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """
    Calculates the total value of a given denomination of bills.

    :param:
        denomination: int - The value of a single bill. This value should be a positive integer.
        number_of_bills: int - The total number of bills. This value should be a positive integer.
    :return:
        int - The calculated value of the bills.

    Example:
    >>> get_value_of_bills(5, 128)
    640
    """

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """
    Calculates the maximum number of bills that can be obtained from a given amount using a specific denomination.

    :param:
        amount: float - The total starting value. This value should be a positive number.
        denomination: int - The value of a single bill. This value should be a positive integer.
    :return:
        int - The number of bills that can be obtained from the given amount. The result is calculated by dividing the amount by the denomination and rounding down to the nearest integer.

    Example:
    >>> get_number_of_bills(127.5, 5)
    25
    """

    return int(amount / denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """
    Calculates the leftover amount after dividing a given amount by a specific denomination of bills.

    :param:
        amount: float - The total starting value. This value should be a positive number.
        denomination: int - The value of a single bill. This value should be a positive integer.
    :return:
        float - The amount that is "leftover", given the current denomination. The result is calculated by finding the remainder of the division of the amount by the denomination.

    Example:
    >>> get_leftover_of_bills(127.5, 20)
    7.5
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param:
        budget: float - the amount of your money you are planning to exchange.
        exchange_rate: float - the unit value of the foreign currency.
        spread: int - percentage that is taken as an exchange fee.
        denomination: int - the value of a single bill.
    :return:
        int - maximum value you can get.

    Example:
    >>> exchangeable_value(127.25, 1.20, 10, 20)
    80
    >>> exchangeable_value(127.25, 1.20, 10, 5)
    95
    """

    exchange_rate += exchange_rate * spread / 100
    exchanged_value = exchange_money(budget, exchange_rate)
    leftover_value = get_number_of_bills(exchanged_value, denomination)
    return leftover_value * denomination
