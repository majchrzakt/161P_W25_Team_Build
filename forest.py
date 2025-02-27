from validate import get_valid_choice

def explore_forest(path):
    """
    Simulates exploring the forest, presenting the user with choices on how to respond to a wild animal.

    Args: path (str): The specific area within the forest being explored.
    Returns (str): A narrative outcome based on the user's choice.

    Behavior:
    Display a blank line
    Display "You walk into the _____ and encounter a wild animal!"" where the blank is the path sent
    Display on a new line "Do you fight, run, or try to negotiate?"
    Set valid_choices equal to "fight run negotiate"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following (where the _____ is the path sent):
      fight --> return the string "You fight bravely in the _____ and win the battle!"
      run --> return the string "You run away safely from the _____, but the adventure ends here."
      negotiate --> return the string "You successfully negotiate with the wild animal and continue your journey!"
    """

