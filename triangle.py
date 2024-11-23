def area(a, b, c):
    if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
        return (a + b + c) / 2


def perimeter(a, b, c):
    if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
        return a + b + c
