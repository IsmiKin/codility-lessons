
def jumping(initial, destination, step):
    distance = destination - initial

    number_of_jumps = int(distance / step)
    if distance % step != 0:
        number_of_jumps = number_of_jumps + 1

    return number_of_jumps
