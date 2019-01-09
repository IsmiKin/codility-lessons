

# O(n + n)
def find_equilibrium_naturals(array_numbers):

    # Calculate the sum of all numbers
    # .. when we reach the half of that sum, it means that in the other half
    # there it's the other one
    full_sum = sum(array_numbers)
    half_full_sum = int(full_sum / 2)

    print('full_sum: {} ; half_full_sum:{}'.format(full_sum, half_full_sum))

    sum_temp = 0
    p_index = 0
    min_difference = None
    # enumerate does not consume O(n), but O(1)
    # .. just in case you want to know the index where to split

    # we iterate doing the sum with each number
    # when we reach the half, we check which index is closer, if the one we
    # found or the previous one
    for index, number in enumerate(array_numbers):
        if (sum_temp + number) > half_full_sum:
            p_index_left = abs(half_full_sum - sum_temp)
            p_index_right = abs(half_full_sum - (sum_temp + number))
            print('sum_temp : {} | p_index_left: {} | p_index_right: {}'.format(
                sum_temp, p_index_left, p_index_right
            ))
            if p_index_left < p_index_right:
                p_index = index - 1
                min_difference = abs((full_sum - sum_temp) - sum_temp)
            else:
                p_index = index
                min_difference = abs(full_sum - (sum_temp + number) - (sum_temp + number))
            break

        sum_temp += number

    return min_difference


def find_equilibrium_integers(array_numbers):
    full_sum = sum(array_numbers)

    min_difference = abs(full_sum)
    sum_left = full_sum
    sum_right = 0

    # array_len = len(array_numbers)
    # for index in range(array_len):
    while len(array_numbers) > 0:
        # import pdb; pdb.set_trace()
        number = array_numbers.pop()
        sum_right += number
        sum_left -= number
        actual_diff = abs(sum_left - sum_right)
        if actual_diff < min_difference:
            min_difference = actual_diff

    return min_difference
