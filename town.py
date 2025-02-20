from validate import get_valid_choice

def explore_town(path):
    """
    Allows the player to choose an activity upon returning to their place in town.

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
        - 'read' or 'book': Start reading 'Legends of the Lost Lands.' A map to a hidden treasure in the mountains falls out.
        - 'watch' or 'show': Watch 'Lord of the Rings' and feel inspired to set out on an adventure.
        - 'sleep': Rest peacefully but wake up feeling like an opportunity was missed.
    - Returns the corresponding narrative string based on the player's choice.

    Example:
        >>> explore_town("Eugene")
        "\nYou head back to your place in Eugene.\nDo you read a book, watch a show, or go to sleep?\n> read\nYou start reading 'Legends of the Lost Lands.' A map to a hidden treasure in the mountains falls out!"
    """
