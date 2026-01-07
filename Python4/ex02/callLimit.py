"""Decorator to limit function calls."""
from typing import Any


def callLimit(limit: int):
    """Return a decorator that limits function calls."""
    count = 0

    def callLimiter(function):
        """Decorate function with call limit."""
        def limit_function(*args: Any, **kwds: Any):
            """Wrapper that enforces call limit."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
