from display import clear_screen
from validate import get_valid_choice
# Lu Wang
def introduction(name):
    """
    Displays the introduction sequence of the Adventure Game and prompts the user to begin.

    Args: name (str) -- The player's name.

    Returns (bool): True if the player is ready to begin; False otherwise.

    Behavior:
    Call clear_screen to clear the screen.
    Display "Welcome to the Adventure Game, _____!" where the _____ is the name entered by the user.
    Display on a new line "Choose your path and actions wisely!"
    Display on a new line "Are you ready to begin? (yes/no)"
    Set valid_choices equal to the string "yes no"
    Set choice equal to what get_valid_choice returns when it's sent valid_choices
    If the "yes" is in choice return true, otherwise display "Maybe next time!" and return false.
    """
    clear_screen()
    print(f"Welcome to the Adventure Game, {name}!")
    print("Choose your path and actions wisely!")
    print("Are you ready to begin? (yes/no)")
    valid_choices = "yes no"
    choice = get_valid_choice(valid_choices)
    if "yes" in choice:
        return True
    else:
        print("Maybe next time!")
        return False

