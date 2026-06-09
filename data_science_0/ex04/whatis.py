import sys

argv = sys.argv
argc = len(argv) - 1

if argc == 0:
    pass

if argc > 1:
    print("AssertionError: more than one argument is provided")
elif argc == 1:
    try:
        number = int(argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
