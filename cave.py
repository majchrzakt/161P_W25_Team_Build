from validate import get_valid_choice


def explore_cave(path):
    """
    Simulates exploring a cave, presenting the user with choices about a treasure chest.

    Args: path (str): The specific location or path within the cave being explored.
    Returns (str): A narrative outcome based on the user's choice.

    Behavior:
    Display a blank line
    Display "You enter the _____ and find a hidden treasure chest!" where the blank is the path sent
    Display on a new line "Do you open the chest, leave it, or try to disarm any traps?"
    Set valid_choices equal to "open leave disarm trap"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following (where the _____ is the path sent):
      open --> return the string "Inside the chest in the _____, you find gold and jewels. You are rich!"
      leave --> return the string "You leave the chest behind in the _____ and walk out."
      disarm or trap --> return the string "You successfully disarm a trap and discover a hidden treasure!"
    """
