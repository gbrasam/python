import sys

argv = sys.argv
argc = len(argv) - 1


try:
    assert argc <= 1, "more than one argument is provided"
    if argc == 1:
        number = int(argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

except AssertionError as error:
    print(f"AssertionError: {error}")

except ValueError:
    print("AssertionError: argument is not an integer")
