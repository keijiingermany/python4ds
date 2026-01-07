"""Functions demonstrating closures."""


def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that applies function repeatedly."""
    count = 0

    def inner() -> float:
        """Apply function to stored value."""
        nonlocal x, count
        x = function(x)
        count += 1
        return x

    return inner


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
