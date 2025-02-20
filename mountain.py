from validate import get_valid_choice

def explore_mountain(path):
    """
    Simulates an adventure scenario where the player explores a mountain path and
    encounters various choices.

    Args:
        path (str): The specific mountain path being explored.

    Returns:
        str: A narrative description of the outcome based on the player's choice.

    Behavior:
    - Presents the player with a scenario upon reaching a high peak on the specified
      mountain path.
    - Offers three choices: 'enjoy the view', 'look for a hidden cave', or 'take a risky leap'.
    - Utilizes the `get_valid_choice` function to validate the player's input against the
      valid choices.
    - Returns a descriptive string corresponding to the player's decision:
        - 'enjoy the view': The player appreciates the scenery and feels at peace.
        - 'look for a hidden cave': The player discovers an ancient cave with mysterious
          markings.
        - 'take a risky leap': The player makes a daring jump, lands safely, and finds a new path.

    Note:
    - The `get_valid_choice` function is responsible for:
        - Displaying a prompt for the player's input.
        - Validating the input against the provided valid choices.
        - Returning the validated choice for further processing.

    Example:
        >>> result = explore_mountain("Rocky Trail")
        (Player is prompted with choices)
        > look for a hidden cave
        >>> print(result)
        You discover an ancient cave with mysterious markings on the walls.

    In this example, the player chooses to look for a hidden cave while exploring the
    'Rocky Trail' path and receives a corresponding narrative outcome.
    """
