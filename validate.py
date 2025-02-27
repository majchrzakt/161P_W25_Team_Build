def get_valid_choice(valid_choices):
    """
    Prompts the user repeatedly to input a choice until a valid one from a set of supplied options is chosen.

    Args: valid_choices (str): A string of valid choices (e.g. 'left right straight').
    Returns (str): The first valid choice that matches the user's input.

    Set valid_words to a list based on what's in valid_choices
    Set valid to False
    As long as valid is False do the following
        Set choice to what the user enters.
        Set choice to all lowercase letters.
        For each word in valid_words:
            if word is in choice return true
        If valid is false, display 'Invalid choice! Please choose from: _____' where the blank is the valid choices.
    Return choice
    """
