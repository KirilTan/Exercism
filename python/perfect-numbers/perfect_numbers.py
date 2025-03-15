from typing import Literal


def classify(n: int) -> Literal["perfect", "abundant", "deficient"]:
    """
    Determine if a number is perfect, abundant, or deficient based on Nicomachus' classification.

    - A number is **perfect** if its aliquot sum equals the number itself.
    - A number is **abundant** if its aliquot sum is greater than the number.
    - A number is **deficient** if its aliquot sum is less than the number.

    :param n: A positive integer.
    :return: One of {"perfect", "abundant", "deficient"}.
    :raises ValueError: If `n` is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum_of_divisors = aliquot_sum(n)

    if sum_of_divisors == n:
        return "perfect"
    elif sum_of_divisors > n:
        return "abundant"
    return "deficient"


def aliquot_sum(n: int) -> int:
    """
    Compute the aliquot sum of a number (sum of proper divisors).

    Optimized to iterate only up to √n to improve efficiency.

    :param n: The number to find the aliquot sum for.
    :return: The sum of proper divisors of `n`.
    """
    if n == 1:
        return 0  # 1 has no proper divisors

    divisors = {1}  # Start with 1, as it's a proper divisor for all numbers > 1

    for i in range(2, int(n**0.5) + 1):  # Iterate only up to √n
        if n % i == 0:
            divisors.add(i)
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                divisors.add(n // i)

    return sum(divisors)


# Example Usage
if __name__ == "__main__":
    test_cases = [6, 12, 28, 15, 496, 8128, 7, 1]
    for num in test_cases:
        print(f"{num} -> {classify(num)}")
