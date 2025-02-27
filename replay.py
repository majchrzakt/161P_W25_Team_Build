from validate import get_valid_choice

def play_again():
    """
    Prompts the player to decide whether to play the game again.

    This function displays a prompt asking the player if they want to play again,
    accepts and validates the player's input, and returns a boolean value based on
    the player's choice.

    Args: None
    Returns (bool): True if the player chooses to play again ('yes'), False otherwise ('no').

    Behavior:
    Display a blank line
    Display "Do you want to play again? (yes/no)"
    Set valid_choices equal to "yes no"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following
      yes --> return true
      no --> display a blank line followed by "Goodbye, adventurer!" and return false
    """
