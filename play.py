from display import clear_screen
from path import choose_path
from forest import explore_forest
from cave import explore_cave
from mountain import explore_mountain
from town import explore_town
from result import display_result

def play_game():
    """
    This function plays the game by getting the initial desired path and starting on
    that chosen path.

    Args: None
    Returns: True if they chose a valid path, Otherwise returns False

    Clear the screen
    Set path to what choose_path returns

    Based on path do one of the following:
      forest --> set result to what explore_forest(path) returns
      cave --> set result to what explore_cave(path) returns
      mountain --> set result to what explore_mountain(path) returns
      town --> set result to what explore_town(path) returns
      otherwise --> print "Invalid choice! Adventure terminated." and return False

    Display results and return True

    """