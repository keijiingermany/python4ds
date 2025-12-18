def main():
    nums = [1, 2, 3]
    words = ["apple", "banana", "mango"]
    price = {"apple": 1, "banana": 2, "mango": 3}

    double = list(map(lambda x: x*2, nums))
    print(double)
    capitalize = list(map(lambda z: z.upper(), words))
    print(list(capitalize))
    print(list(price.items()))
    print(list(filter(lambda a: a % 2 == 1, nums)))


if __name__ == "__main__":
    main()
