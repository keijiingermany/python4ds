import sys
import string


def count_charaters(text: str) -> None:
""" a function to count a string character"""

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    args = sys.argv[1:]
    if len(args) > 1:
        print("AssertationError: more than one argument is provided")
        return
    if len(args) == 0:
        text = input("What is the text to count?")
    else:
        text = args[0]
    count_charaters(text)


if __name__ == "__main__":
    main()
