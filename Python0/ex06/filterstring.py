import sys
from ft_filter import ft_filter


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("AssertionError: the arguments are bad")
        return

    s, n = args[0], args[1]

    try:
        n = int(n)
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = s.split(" ")

    filtered = [w for w in ft_filter(lambda x: len(x) > n, words)]

    print(filtered)


if __name__ == "__main__":
    main()
