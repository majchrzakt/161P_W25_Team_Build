from validate import get_valid_choice

def play_again():
    """
    Prompts the player to decide whether to play the game again.

    This function displays a prompt asking the player if they want to play again,
    accepts and validates the player's input, and returns a boolean value based on
    the player's choice.

    Args:
        None

    Returns:
        bool: True if the player chooses to play again ('yes'), False otherwise ('no').

    Behavior:
    - Displays the prompt: "Do you want to play again? (yes/no)".
    - Defines valid choices as: 'yes' and 'no'.
    - Utilizes the `get_valid_choice` function to obtain and validate the player's input.
    - If the player inputs 'yes', returns True.
    - If the player inputs 'no':
        - Prints a farewell message: "Goodbye, adventurer!".
        - Returns False.

    Note:
    - The `get_valid_choice` function is responsible for:
        - Displaying a prompt for the player's input.
        - Validating the input against the provided valid choices.
        - Returning the validated choice for further processing.

    Example:
        >>> play_again()
        Do you want to play again? (yes/no)
        > yes
        True

        >>> play_again()
        Do you want to play again? (yes/no)
        > no
        Goodbye, adventurer!
        False

    In these examples, the function prompts the player to decide whether to play again
    and returns a boolean value based on the player's input.
    """
