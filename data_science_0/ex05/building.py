import sys


def is_punctuation(character) -> bool:
    """
    Check whether a character is punctuation.
    Return True if the character is a punctuation mark.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return character in punctuation


def counter(text):
    """
    Count character categories in text.
    """
    total_characters = len(text)
    count_upper = 0
    count_lower = 0
    count_digits = 0
    count_spaces = 0
    count_punctuation = 0

    for c in text:
        if c.isupper():
            count_upper += 1
        elif c.islower():
            count_lower += 1
        elif c.isdigit():
            count_digits += 1
        elif c.isspace():
            count_spaces += 1
        elif is_punctuation(c):
            count_punctuation += 1

    print(f"The text contains {total_characters} characters:")
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punctuation} punctuation marks")
    print(f"{count_spaces} spaces")
    print(f"{count_digits} digits")


def main():
    """
    Check arguments, get the input text, and display character statistics.
    """
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("What is the text to count?")
        try:
            text = input()
            text += "\n"
            counter(text)
        except EOFError:
            pass
    elif argc > 1:
        print("AssertionError: more than one argument is provided")
    else:
        counter(argv[1])


if __name__ == "__main__":
    main()
