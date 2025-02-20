def get_valid_choice(valid_choices):
    """
    Prompts the user to input a choice and validates it against a set of valid options.

    This function repeatedly prompts the user for input until a valid choice is entered.
    It checks if any of the valid options are present in the user's input (case-insensitive)
    and returns the first matching choice.

    Args:
        valid_choices (str): A space-separated string of valid choices.

    Returns:
        str: The first valid choice that matches the user's input.

    Behavior:
    - Splits the `valid_choices` string into a list of valid options.
    - Repeatedly prompts the user for input until a valid choice is entered.
    - Returns the first valid choice that matches the user's input.

    Example:
        >>> get_valid_choice("yes no")
        > yes
        'yes'
    """
