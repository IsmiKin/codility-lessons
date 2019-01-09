

def find_missing_element(array_elements):
    n = len(array_elements)
    total = (n+1)*(n+2)/2

    sum_of_array_elements = sum(array_elements)
    return total - sum_of_array_elements
