def is_armstrong_number(number: int) -> bool:
    power_of = len(str(number))
    total_sum = 0

    for current_number in str(number):
        total_sum += pow(int(current_number), power_of)

    return total_sum == int(number)
