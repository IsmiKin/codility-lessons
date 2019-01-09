
# Find the smallest positive integer (not 0) that doesn't occurr in the array


def find_missing_integer(array_numbers):
    # We could improve memory complexity just taking the max and doing
    # an array of booleans with just [1... max], but it would take O(n)

    # existence_boolean_array = [False for x in xrange(max(array_numbers))]
    max_number = max(array_numbers)

    if max_number < 0:
        return 1

    # We use max instead of length because we are goin to ignore the negatives
    existence_boolean_array = [False for x in range(max(array_numbers) + 1)]
    for number in array_numbers:
        if number > 0:
            existence_boolean_array[number] = True

    # import pdb; pdb.set_trace()
    min_missing_positive = None
    for number, exists in enumerate(existence_boolean_array):
        if not exists:
            min_missing_positive = number

    return min_missing_positive
