def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and print its shape information.

    Args:
        family: 2D list (array) to be sliced
        start: Starting index for slicing
        end: Ending index for slicing

    Returns:
        Truncated version of the array based on start and end indices
    """

    if not isinstance(family, list):
        print("Error: Family must be a list")
        return None

    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: Start and end must be integers")
        return None

    if len(family) == 0:
        print("Error: List cannot be empty")
        return None

    if not all(isinstance(row, list) for row in family):
        print("Error: All elements must be lists (2D array required)")
        return None

    if len(family) > 0:
        first_row_len = len(family[0])
        if not all(len(row) == first_row_len for row in family):
            print("Error: All rows must have the same length")
            return None

    rows = len(family)
    cols = len(family[0]) if rows > 0 else 0
    print(f"My shape is : ({rows}, {cols})")

    truncated = family[start:end]

    new_rows = len(truncated)
    new_cols = len(truncated[0]) if new_rows > 0 else 0
    print(f"My new shape is : ({new_rows}, {new_cols})")

    return truncated
