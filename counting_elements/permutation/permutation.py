

# Given an array of numbers, check if it's a permutation
# A permutation is a set of numbers that it's not miss any number in the
# and it has an occurrence of each number only once
# sequence, like 3,2,4

def is_permutation(array):
    # Can be improved doing one loop and fetching min and max same time
    # Probably there is a better way than just doin a set
    return max(array) - min(array) + 1 == len(set(array))
