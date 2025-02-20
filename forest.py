from validate import get_valid_choice

def explore_forest(path):
    """
    Simulates an encounter in the forest, presenting the user with choices
    on how to respond to a wild animal.

    Args:
        path (str): The specific path or area within the forest being explored.

    Returns:
        str: A narrative description of the outcome based on the user's choice.

    Behavior:
    - Displays a scenario where the user encounters a wild animal in the specified path.
    - Prompts the user to choose an action: 'fight', 'run', or 'negotiate'.
    - Utilizes the `get_valid_choice` function to validate user input against the valid choices.
    - Returns a descriptive string based on the user's choice:
        - 'fight': Describes a victorious battle with the wild animal.
        - 'run': Indicates a safe retreat, ending the adventure.
        - 'negotiate': Details a successful negotiation, allowing the journey to continue.

    Note:
    The `get_valid_choice` function is responsible for:
    - Prompting the user for input until a valid choice is made.
    - Converting user input to lowercase to ensure case-insensitive matching.
    - Checking if the user's input contains any of the valid choices.
    - Returning the valid choice once obtained.

    Example:
        >>> explore_forest("dense thicket")
        You walk into the dense thicket and encounter a wild animal!
        Do you fight, run, or try to negotiate?
        > fight
        'You fight bravely in the dense thicket and win the battle!'
    """

