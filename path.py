from display import clear_screen
from validate import get_valid_choice

def choose_path():
    """
    Presents the player with a crossroads scenario and prompts them to choose a direction.

    This function clears the screen, describes the current situation where the player is at a
    crossroads, and offers four directional choices: left, right, straight ahead, or back. Based
    on the player's input, it returns the corresponding path identifier.

    Args: None
    Returns (str): The chosen path of either forest, cave, mountain, town, or an empty string.

    Behavior:
    Call clear_screen to clear the screen.
    Display "You find yourself at a crossroads."
    Display on a new line "Do you want to go left, right, straight ahead, or turn back?"
    Set valid_choices equal to "left right straight ahead back"
    Set choice equal to the value returned by get_valid_choice when it's sent valid_choices

    Based on the value of choice do one of the following
      left --> return the string "forest"
      right --> return the string "cave"
      straight or ahead --> return the string "mountain"
      back --> return the string "town"
      otherwise --> return the string ""
    """

    clear_screen()
    print("You find yourself at a crossroads.\n"
          "You can still hear the bustle of the town you left behind, as you look ahead see ahead, where your path becomes steeper and more rugged.\n"
          "From your left you hear bright chirping - accompanied by the gentle, constant creaking of old woods.\n"
          "To your right you see the entrance to a wet and dark cave.")

    valid_choices = "left right straight ahead back"
    #print (f"in path.py valid_choices is {valid_choices}")
    print("Do you want to go left, right, straight ahead, or turn back?")
    choice = get_valid_choice(valid_choices)
    if choice == "left":
        return "forest"
    elif choice == "right":
        return "cave"
    elif choice == "straight" or "ahead":
        return "mountain"
    elif choice == "back":
        return "town"
    else:
        return ""
