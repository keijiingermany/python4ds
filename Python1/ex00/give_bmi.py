def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.

    Args:
        height: List of heights in meters
        weight: List of weights in kilograms

    Returns:
        List of BMI values (weight / height^2)
    """

    if not isinstance(height, list) or not isinstance(weight, list):
        print("Both height and weight must be lists")
        return None

    if len(height) != len(weight):
        print("Height and weight lists must have the same length")
        return None

    if len(height) == 0:
        print("Lists cannot be empty")
        return None

    bmi_list = []

    for h, w in zip(height, weight):

        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("All values must be integers or floats")
            return None

        if h <= 0:
            print("Height must be positive")
            return None
        if w <= 0:
            print("Weight must be positive")
            return None

        bmi = w / (h ** 2)
        bmi_list.append(bmi)

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values are above a given limit.

    Args:
        bmi: List of BMI values
        limit: Threshold value to compare against

    Returns:
        List of booleans (True if BMI > limit, False otherwise)
    """

    if not isinstance(bmi, list):
        print("BMI must be a list")
        return None

    if not isinstance(limit, (int, float)):
        print("Limit must be an integer or float")
        return None

    result = []

    for value in bmi:
        # Check if each value is numeric
        if not isinstance(value, (int, float)):
            print("All BMI values must be integers or floats")
            return None

        # Compare with limit
        result.append(value > limit)

    return result
