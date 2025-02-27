from validate import get_valid_choice

def explore_town(path):
    print("\n")
    print(f"You head back to your place in {path}")

    valid_choices = ["read", "book", "watch", "show", "sleep"]

    action = input("Do you read a book, watch a show, or go to sleep?")
    valid = False
    while not valid:
        if action in valid_choices:
            if action == "read" or action == "book":
                return ("You start reading 'Legends of the Lost Lands'."
                        "A map to a hidden treasure in the mountains falls out!")
            elif action == "watch" or action == "show":
                return "You watch 'Lord of the Rings' and are inspired to set out on an adventure of your own."
            elif action == "sleep":
                return "You rest peacefully, but wake up the next day feeling like you missed an opportunity."
        else:
            action = input("Invalid input you geezer, please enter a proper action yeah?")
    """
    Allows the player to choose an activity upon returning to their place in town.

    Args: path (str): The name of the player's place in town.
    Returns (str): A narrative outcome based on the user's choice.

    Behavior:
    Display a blank line
    Display "You head back to your place in _____" where the blank is the path sent
    Display on a new line "Do you read a book, watch a show, or go to sleep?"
    Set valid_choices equal to "read book watch show sleep"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following (where the _____ is the path sent):
      read or book --> return the string "You start reading 'Legends of the Lost Lands.'
        A map to a hidden treasure in the mountains falls out!"
      watch or show --> return the string "You watch 'Lord of the Rings' and are inspired to
        set out on an adventure of your own."
      sleep --> return the string "You rest peacefully, but wake up the next day feeling like
        you missed an opportunity."




    This function presents the player with a set of activities to choose from after
    returning to their place in town. Based on the player's choice, it returns a
    corresponding narrative string.

    Args:
        path (str): The name of the player's place in town.

    Returns:
        str: A narrative string describing the outcome of the chosen activity.

    Behavior:
    - Displays a prompt indicating the player has returned to their place in town.
    - Presents the following activity choices:
        - 'read' or 'book': Start reading 'Legends of the Lost Lands.'
                            A map to a hidden treasure in the mountains falls out.
        - 'watch' or 'show': Watch 'Lord of the Rings' and feel inspired to set out on an adventure.
        - 'sleep': Rest peacefully but wake up feeling like an opportunity was missed.
    - Returns the corresponding narrative string based on the player's choice.

    Example:
        >>> explore_town("Eugene")
        "\n
        You head back to your place in Eugene.\n
        Do you read a book, watch a show, or go to sleep?\n
        > read\n
        You start reading 'Legends of the Lost Lands.'
        A map to a hidden treasure in the mountains falls out!"
    """
