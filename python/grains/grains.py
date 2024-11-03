def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total(board_size: int = 64) -> int:
    if board_size < 1 or board_size > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** board_size - 1
