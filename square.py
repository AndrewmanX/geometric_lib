def area(a):
    if a < 0:
        raise AssertionError("Side length cannot be negative")
    if a == 0:
        return 0
    return a * a


def perimeter(a):
    if a < 0:
        raise AssertionError("Side length cannot be negative")
    if a == 0:
        return 0
    return 4 * a
