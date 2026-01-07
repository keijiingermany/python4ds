"""Calculate statistics from arguments."""
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate statistics based on kwargs instructions."""
    # Error handling: no args
    if not args:
        for _ in kwargs.values():
            print("ERROR")
        return

    # Error handling: no kwargs
    if not kwargs:
        return

    # Convert to numbers
    try:
        data = sorted([float(x) for x in args])
    except (ValueError, TypeError):
        for _ in kwargs.values():
            print("ERROR")
        return

    n = len(data)

    # Process each requested statistic
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
            print(f"median : {median}")

        elif value == "quartile":
            # Quartile: 25% = index 1, 75% = index 3 for 5 elements
            # Using simple indexing for quartiles
            q1 = data[int(n * 0.25)]
            q3 = data[int(n * 0.75)]
            print(f"quartile : [{float(q1)}, {float(q3)}]")

        elif value == "std":
            # Standard deviation (population)
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            std = variance ** 0.5
            print(f"std : {std}")

        elif value == "var":
            # Variance (population)
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            print(f"var : {variance}")


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
