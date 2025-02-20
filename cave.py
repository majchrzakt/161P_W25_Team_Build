from validate import get_valid_choice


def explore_cave(path):
    """
    Simulates an exploration scenario within a cave, presenting the user with choices
    regarding a discovered treasure chest.

    Args:
        path (str): The specific location or path within the cave being explored.

    Returns:
        str: A narrative outcome based on the user's decision.

    Behavior:
    - Displays a scenario where the user encounters a treasure chest in the specified path.
    - Prompts the user to choose an action: 'open', 'leave', or 'disarm trap'.
    - Utilizes the `get_valid_choice` function to validate user input against the valid choices.
    - Returns a descriptive string based on the user's choice:
        - 'open': Describes finding wealth inside the chest.
        - 'leave': Indicates the chest was left untouched.
        - 'disarm trap': Details the successful disarmament of a trap and discovery of treasure.

    Note:
    The `get_valid_choice` function is responsible for:
    - Prompting the user for input until a valid choice is made.
    - Converting user input to lowercase to ensure case-insensitive matching.
    - Checking if the user's input contains any of the valid choices.
    - Returning the valid choice once obtained.

    Example:
        >>> explore_cave("dark tunnel")
        You enter the dark tunnel and find a hidden treasure chest!
        Do you open the chest, leave it, or try to disarm any traps?
        > open
        'Inside the chest in the dark tunnel, you find gold and jewels. You are rich!'
    """
