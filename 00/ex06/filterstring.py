import sys
from ft_filter import ft_filter


def main():
    """Entry point of the program
    """
    try:
        if len(sys.argv) == 3:
            S = sys.argv[1]
            N = int(sys.argv[2])
            words = S.split()
            res = ft_filter(lambda word: len(word) > N, words)
            print(res)
        else:
            assert False, "the arguments are bad"
    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
