def area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise AssertionError("Invalid triangle sides")
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise AssertionError("Invalid triangle sides")
    return a + b + c
