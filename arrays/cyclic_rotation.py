def solution(A, K):
    # write your code in Python 3.6
    # print('Initial array: {}'.format(A))
    array_length = len(A)
    result_array = A
    iterator = 0
    while iterator < K:
        # print('Array after {} iterations'.format(iterator))
        # print('{}'.format(result_array))
        previous_array = result_array.copy()
        # print('Previous array {}'.format(previous_array))
        result_array = previous_array[:-1]
        result_array.insert(0, previous_array[-1:][0])
        iterator = iterator + 1

    return result_array
