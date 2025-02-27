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


def explore_cave(path):
    """
    Simulates an exploration scenario within a cave, presenting the user with choices
    regarding a discovered treasure chest.

    Args:
        path (str): The specific location or path within the cave being explored.

    Returns:
        str: A narrative outcome based on the user's decision.
    """
    print(f"You venture deep into the cave through the {path}.")
    print("As you move forward, you discover a mysterious treasure chest!")

    choice = input("Do you want to open the chest? (yes/no): ").strip().lower()

    if choice == "yes":
        return open_chest()
    elif choice == "no":
        return leave_chest()
    else:
        return "Uncertain of what to do, you hesitate, and the cave suddenly rumbles... Maybe next time you'll decide quicker!"


def open_chest():
    """
    Handles the scenario where the user chooses to open the treasure chest.

    Returns:
        str: A description of what happens when the chest is opened.
    """
    print("You cautiously open the chest...")
    outcomes = [
        "Inside, you find a pile of gold and ancient artifacts!",
        "A cloud of dust bursts out, revealing... nothing! It was just an empty chest.",
        "A hidden mechanism triggers, and a swarm of bats flies out, startling you!"
    ]

    import random
    return random.choice(outcomes)


def leave_chest():
    """
    Handles the scenario where the user decides not to open the treasure chest.

    Returns:
        str: A description of what happens when the chest is left alone.
    """
    return "You decide it's best not to tamper with unknown treasures and leave the cave safely."


# Example usage:
if __name__ == "__main__":
    cave_path = input("Enter the path you are exploring in the cave: ")
    result = explore_cave(cave_path)
    print(result)

