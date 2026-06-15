import numpy as np


def validate_numeric_list(values: list[int | float]) -> bool:
    """check if all values in a list are integers or floats"""

    for value in values:
        if isinstance(value, bool):
            return False
        if not isinstance(value, (int, float)):
            return False
    return True


def validate_2d_list(family: list) -> bool:
    """
    check if family is a non-empty 2D list of numeric values.
    it checks:
    family is a list
    family is not empty
    each row is a list
    each row is not empty
    each value is numeric
    """

    if not isinstance(family, list):
        return False

    if not family:
        return False

    for item in family:
        if not isinstance(item, list):
            return False
        if not item:
            return False
        if not validate_numeric_list(item):
            return False

    return True


def validate_row_lengths(family: list) -> bool:
    """check if all rows in family have the same length"""

    reference_length = len(family[0])
    for item in family:
        if len(item) != reference_length:
            return False

    return True


def validate_integer(value: int) -> bool:
    """check if value is an integer"""

    if type(value) is not int:
        return False

    return True


def validate_arguments(family: list, start: int, end: int) -> None:
    """validate family, start and end arguments"""

    if not validate_2d_list(family):
        raise ValueError("family must be a non-empty list of numeric lists")

    if not validate_row_lengths(family):
        raise ValueError("all rows must have the same size")

    if not validate_integer(start):
        raise ValueError("start must be an integer")

    if not validate_integer(end):
        raise ValueError("end must be an integer")


def slice_me(family: list, start: int, end: int) -> list:
    """
    print the shape of a 2D list, slice it from start to end,
    print the new shape and return the sliced list
    """

    try:
        validate_arguments(family, start, end)

        family_array = np.array(family)
        print(f"My shape is : {family_array.shape}")

        new_family = family_array[start:end]
        print(f"My new shape is : {new_family.shape}")
        return new_family.tolist()

    except ValueError as error:
        print(f"AssertionError: {error}")
        return []
