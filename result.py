from validate import get_valid_choice

adef display_result(result):
    """
    Displays the provided result string within a decorative border of asterisks.

    This function takes a string input, calculates its length, and prints a border of asterisks
    above and below the result string. The border length is equal to the length of the result
    string plus four additional asterisks for padding.

    Args:
        result (str): The string to be displayed within the decorative border.

    Returns:
        None

    Behavior:
    - Calculates the length of the `result` string.
    - Prints a line of asterisks with a length of `res_len + 4`, where `res_len` is the length
      of the `result` string.
    - Prints the `result` string, centered within the border.
    - Prints another line of asterisks identical to the first.

    Example:
        >>> display_result("Congratulations!")
        ****
        Congratulations!
        ****
    """
