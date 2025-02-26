# numbers_phrases = {
#     3 : 'Pling',
#     5 : 'Plang',
#     7 : 'Plong',
# }
#
# def convert(n: int) -> str:
#     result = []
#     for number, phrase in numbers_phrases.items():
#         if divisible_by(n, number):
#             result.append(phrase)
#
#     if not result:
#         return str(n)
#     return ''.join(result)
#
# def divisible_by(number: int, divisor: int) -> bool:
#     return number % divisor == 0

from typing import Dict

# Constants
NUMBERS_PHRASES: Dict[int, str] = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(n: int) -> str:
    """
    Converts a number to its corresponding raindrop sounds. If the number does not correspond to a raindrop sound,
    returns the number as a string.

    :param n: The input number.
    :return: Raindrop sound or the number as a string.
    """
    result = "".join(phrase for number, phrase in NUMBERS_PHRASES.items() if n % number == 0)
    return result or str(n)


# Example Usage
if __name__ == "__main__":
    test_cases = [28, 30, 34, 105, 7, 15, 21]
    for num in test_cases:
        print(f"{num} -> {convert(num)}")
