def is_even(value):
    return (value & 1) == 0


def is_even2(value):
    value = abs(value)
    odd = True
    for _ in range(value):
        odd = not odd
    return odd
