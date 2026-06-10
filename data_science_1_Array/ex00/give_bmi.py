import numpy as np


def validate_numeric_list(values):



def argument_checkpoint(height: list[int | float],
                        weight: list[int | float]):
    if type(height) is not list or type(weight) is not list:
        print("both arguments must be lists")

    if len(height) != len(weight):
        print("both lists must have the same length")
    
    try:
        validate_numeric_list(height)
        validate_numeric_list(weight)
    
    except ValueError:
        print("AssertionError: argument is not an integer")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    BMI (Body Mass Index) is a value calculated from:
    BMI = weight / height²
    """

    argument_checkpoint(height, weight)



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """XXXXXXXX"""



def main():
    """XXXXXXXX"""





if __name__ == "__main__":
    main()
