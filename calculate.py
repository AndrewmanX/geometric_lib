import circle
import square

FIGS = ["circle", "square", "triangle"]
FUNCS = ["perimeter", "area"]
SIZES = {
    "circle-area": 1,
    "circle-perimeter": 1,
    "square-area": 1,
    "square-perimeter": 1,
    "triangle-area": 3,
    "triangle-perimeter": 3,
}


def calc(fig, func, size):
    assert fig in FIGS, f"Unsupported figure: {fig}"
    assert func in FUNCS, f"Unsupported function: {func}"

    key = f"{fig}-{func}"
    expected_args = SIZES.get(key)
    assert expected_args is not None, f"Unsupported operation: {key}"
    assert (
            len(size) == expected_args
    ), f"Expected {expected_args} arguments, got {len(size)}"

    assert all(s >= 0 for s in size), "All sizes must be non-negative"

    # Validate triangle inequality
    if fig == "triangle":
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle sides"

    # Perform calculation
    if fig == "circle":
        if func == "area":
            return circle.area(*size)
        elif func == "perimeter":
            return circle.perimeter(*size)
    elif fig == "square":
        if func == "area":
            return square.area(*size)
        elif func == "perimeter":
            return square.perimeter(*size)
    elif fig == "triangle":
        if func == "area":
            a, b, c = size
            s = (a + b + c) / 2  # Полупериметр
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        elif func == "perimeter":
            return sum(size)

    raise AssertionError(f"Unhandled case for {fig} with {func}")


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    # Get figure name
    while fig not in FIGS:
        fig = input(f"Enter figure name, available"
                    f" are {FIGS}:\n").strip().lower()

    # Get function name
    while func not in FUNCS:
        func = input(f"Enter function name, "
                     f"available are {FUNCS}:\n").strip().lower()

    # Get sizes
    expected_size = SIZES.get(f"{fig}-{func}", 1)
    while len(size) != expected_size:
        try:
            size = list(
                map(
                    int,
                    input(
                        f"Input {expected_size}"
                        f" figure sizes separated by space:\n"
                    ).split(),
                )
            )
        except ValueError:
            print("Invalid input. Please enter integers only.")
            size = []

    # Perform calculation
    result = calc(fig, func, size)
    print(f"The result of {func} for {fig} with size {size} is: {result}")
