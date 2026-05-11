import sys


def count(object: any) -> tuple:
    """
    goes through the char and increase the counters by category
    """
    digit_count = 0
    lower_count = 0
    upper_count = 0
    punctuation_count = 0
    space_count = 0
    total_count = 0
    for char in object:
        total_count += 1
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        else:
            punctuation_count += 1
    return upper_count, lower_count, punctuation_count, \
        space_count, digit_count, total_count


def main():
    """Entry point of the program
    """
    try:
        if len(sys.argv) == 1:
            res = input("What is the text to count?\n")
            # input stripe automatiquement le /n
        elif len(sys.argv) == 2:
            res = str(sys.argv[1])
        else:
            assert False, "more than one argument is provided"
        result = count(res)
        print(f"The text contains {result[5]} characters:")
        print(f"{result[0]} upper letters")
        print(f"{result[1]} lower letters")
        print(f"{result[2]} punctuation marks")
        print(f"{result[3]} spaces")
        print(f"{result[4]} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
