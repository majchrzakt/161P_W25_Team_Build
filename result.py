from validate import get_valid_choice
def display_result(result):
    """
    Displays the provided result string within a decorative border of asterisks.

    This function takes a string input, calculates its length, and prints a border of asterisks
    above and below the result string. The border length is equal to the length of the result
    string plus four additional asterisks for padding.

    Args: result (str): The string to be displayed within the decorative border.
    Returns: None

    Behavior:
    Set res_len to the length of result
    Display on a new line x+4 asterisks where x is the number of letters in result
    Display on a new line two blank spaces followed by what's stored in result
    Display on a new line x+4 asterisks where x is the number of letters in result
    Display a blank line
    """
    res_len = len(result)
    print(f"\n****", end="")
    for _ in range(res_len):
        print("*", end="")

    print(f"\n  {result}")
    print("****", end="")

    for _ in range(res_len):
        print("*", end="")

    print()
