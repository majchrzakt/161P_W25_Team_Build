from validate import get_valid_choice

def explore_mountain(path):
    """
    Simulates exploring a mountain path where the user is presented with choices.

    Args: path (str): The specific moutain path being explored.
    Returns (str): A narrative outcome based on the user's choice.

    Behavior:
    Display a blank line
    Display "You climb the _____ and reach a high peak!" where the blank is the path sent
    Display on a new line "o you enjoy the view, look for a hidden cave, or take a risky leap?"
    Set valid_choices equal to "enjoy view look cave leap"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following (where the _____ is the path sent):
      enjoy or view --> return the string "You enjoy the breathtaking view from the _____ and feel at peace."
      look or cave --> return the string "You discover an ancient cave with mysterious markings on the walls."
      leap --> return the string "You take a leap and successfully land on a ledge below, finding a new path."
    """
