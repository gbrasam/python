
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


def validate_arguments(family: list, start: int, end: int) -> None:
    """validate family, start and end arguments"""

    if not validate_2d_list(family):
        raise ValueError("family must be a non-empty list of numeric lists")

    if not validate_row_lengths(family):
        raise ValueError("all rows must have the same size")

    # later: validate start and end


def slice_me(family: list, start: int, end: int) -> list:
    """
    print the shape of a 2D list and return a slice
    between the specified start and end indices
    """

    try:
        validate_arguments(family, start, end)
        #WIP
    except ValueError as error:
        print(f"AssertionError: {error}")
        return []
