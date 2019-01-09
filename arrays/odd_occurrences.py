# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    number_of_pairs = int(len(A)/2)
    #print('Max num of pairs: {}'.format(number_of_pairs))

    paired_numbers = set([])
    not_paired_numbers = []
    result_number = None

    for number in A:
        if number in not_paired_numbers:
            not_paired_numbers.remove(number)
            paired_numbers.add(number)
        elif number not in paired_numbers:
            not_paired_numbers.append(number)

    #print('Paired numbers {}'.format(paired_numbers))
    #print('Not paired numbers {}'.format(not_paired_numbers))

    return not_paired_numbers.pop()
