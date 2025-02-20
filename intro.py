from display import clear_screen
from validate import get_valid_choice

def introduction(name):
    """
    Displays the introduction sequence of the Adventure Game and prompts the user to begin.

    Args:
        name (str): The player's name.

    Returns:
        bool: True if the player is ready to begin; False otherwise.

    Behavior:
    - Clears the console screen using the `clear_screen` function.
    - Greets the player by name and provides introductory information about the game.
    - Prompts the player with the question: "Are you ready to begin? (yes/no)"
    - Utilizes the `get_valid_choice` function to validate user input against the choices "yes" or "no".
    - Returns True if the player chooses "yes", allowing the game to proceed.
    - Prints "Maybe next time!" and returns False if the player chooses "no", terminating the game.

    Note:
    - The `clear_screen` function is expected to clear the console output to provide a clean interface.
    - The `get_valid_choice` function is responsible for:
        - Prompting the user for input until a valid choice ("yes" or "no") is made.
        - Converting user input to lowercase to ensure case-insensitive matching.
        - Returning the valid choice once obtained.

    Example:
        >>> introduction("Alice")
        (Clears the screen)
        Welcome to the Adventure Game, Alice!
        Choose your path and actions wisely!
        Are you ready to begin? (yes/no)
        > yes
        True

        >>> introduction("Bob")
        (Clears the screen)
        Welcome to the Adventure Game, Bob!
        Choose your path and actions wisely!
        Are you ready to begin? (yes/no)
        > no
        Maybe next time!
        False
    """
