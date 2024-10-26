def steps(number, memo={}):
    # Raise an error for non-positive integers
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    loops = 0
    original_number = number

    # Use memoized results if they exist
    if number in memo:
        return memo[number]

    while number != 1:
        if number % 2 == 0:  # Even number
            number //= 2
        else:  # Odd number
            number = number * 3 + 1

        loops += 1

        # Check if the current number has been computed before
        if number in memo:
            loops += memo[number]
            break

    # Store the result in the memo dictionary
    memo[original_number] = loops
    return loops
