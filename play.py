from display import clear_screen
from path import choose_path
from forest import explore_forest
from cave import explore_cave
from mountain import explore_mountain
from town import explore_town
from result import display_result


# Function 7: Play game (coordinates all the functions together)
def play_game():
    clear_screen()
    path = choose_path()

    if path == "forest":
        result = explore_forest(path)
    elif path == "cave":
        result = explore_cave(path)
    elif path == "mountain":
        result = explore_mountain(path)
    elif path == "town":
        result = explore_town(path)
    else:
        print("Invalid choice! Adventure terminated.")
        return False

    display_result(result)
    return True