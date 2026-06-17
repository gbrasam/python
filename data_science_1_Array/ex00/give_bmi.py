import numpy as np


def validate_numeric_list(values: list[int | float]) -> bool:
    """check if all values in a list are int or float"""

    for value in values:
        if isinstance(value, bool):
            return False
        if not isinstance(value, (int, float)):
            return False

    return True


def validate_arguments(height: list[int | float],
                       weight: list[int | float]) -> None:
    """validate arguments for BMI calculation"""

    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("both arguments must be lists")

    if not height or not weight:
        raise ValueError("height and weight cannot be empty")

    if len(height) != len(weight):
        raise ValueError("both lists must have the same length")

    if not validate_numeric_list(height):
        raise ValueError("height contains non numeric values")

    if not validate_numeric_list(weight):
        raise ValueError("weight contains non numeric values")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    it takes 2 lists of integers or floats in input
    and returns a list of BMI values
    BMI (Body Mass Index) is a value calculated from:
    BMI = weight / height²
    """

    try:
        validate_arguments(height, weight)

        height_array = np.array(height)
        weight_array = np.array(weight)

        if np.any(height_array == 0):
            raise ValueError("height cannot be equal to 0")
        bmi = weight_array / (height_array ** 2)

        return bmi.tolist()

    except ValueError as error:
        print(f"AssertionError: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans indicating whether each BMI
    value is greater than the specified limit.
    """

    try:
        if not isinstance(bmi, list):
            raise ValueError("bmi must be a list")

        if not validate_numeric_list(bmi):
            raise ValueError("bmi contains non numeric values")

        if not isinstance(limit, int) or isinstance(limit, bool):
            raise ValueError("limit must be an integer")

        return [value > limit for value in bmi]

    except ValueError as error:
        print(f"AssertionError: {error}")
        return []
