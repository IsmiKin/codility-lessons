def solution(A):
    # write your code in Python 3.6
    big_set = set(range(1,1000000))
    small_set = set(A)
    intersection = big_set.difference(small_set)

    if intersection is None:
        return 1
    else:
        return next(iter(intersection))
