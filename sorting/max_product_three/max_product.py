
# thee maximal product of any triplet.
# A non-empty array A consisting of N integers is given.
# The product of triplet (P, Q, R)
# equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

# Solution wrong: I missunderstood, i thought it was required bigger multiplitaction POSSITIVE
def max_product_of_three(array):
    array.sort()  # O(n*logn)
    print(array)
    # we have to iterate from the beginning and end and try to avoid the 0
    # we will compare the numbers in both sides (minimums and maximums)
    # and compare in abs to get the biggest, and also the sign at that time
    # True = positive, False = negative
    multipliers_counter = 0
    left_index = 0
    right_index = len(array) - 1

    max_product_of_three_mul = 1
    sign = True

    left_number = array[left_index]
    right_number = array[right_index]

    while multipliers_counter < 3 and left_index < right_index:

        # right number shouldn't be negative, but just in case
        if abs(left_number) >= abs(right_number) and not(multipliers_counter == 2 and sign):
            next_multiplier = left_number
            sign = not sign
            left_index += 1
            left_number = array[left_index]
        else:
            next_multiplier = right_number
            right_index -= 1
            right_number = array[right_index]

        multipliers_counter += 1
        max_product_of_three_mul *= next_multiplier

    return max_product_of_three_mul
