import sys


NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def encode_morse(text: str) -> str:
""" function translating string into morse code """

    result = []
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        result.append(NESTED_MORSE[char])
    return " ".join(result)


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    arg = sys.argv[1]

    try:
        print(encode_morse(arg))
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
