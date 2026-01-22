"""Calculate statistics from arguments."""
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate statistics based on kwargs instructions."""
    if not kwargs:
        return

    if not args:
        for _ in kwargs.values():
            print("ERROR")
        return

    try:
        data = sorted([float(x) for x in args])
    except Exception:
        for _ in kwargs.values():
            print("ERROR")
        return

    n = len(data)

    for value in kwargs.values():
        if value == "mean":
            mean = sum(data) / n
            print(f"mean : {mean}")

        elif value == "median":
            mid = n // 2
            if n % 2 == 0:
                median = (data[mid - 1] + data[mid]) / 2
            else:
                median = data[mid]

            if median.is_integer():
                print(f"median : {int(median)}")
            else:
                print(f"median : {median}")

        elif value == "quartile":
            q1 = data[n // 4]
            q3 = data[(n * 3) // 4]
            print(f"quartile : [{float(q1)}, {float(q3)}]")

        elif value == "std":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            std = variance ** 0.5
            print(f"std : {std}")

        elif value == "var":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            print(f"var : {variance}")


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
