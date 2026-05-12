import sys


def makeitmorse(S) -> str:
    """receive a string and turn it into morse
    also store the dictionnary"""
    NESTED_MORSE = {" ": "/ ",
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
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    "0": "-----"}
    separat = " "
    newS = separat.join([NESTED_MORSE[char.upper()] for char in S])
    return newS


def main():
    """Entry point of the program
    """
    try:
        if len(sys.argv) == 2:
            S = sys.argv[1]
            assert all(char.isalnum() or char == " " for char in S), \
                "the arguments are bad"
            res = makeitmorse(S)
            print(res)
        else:
            assert False, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
