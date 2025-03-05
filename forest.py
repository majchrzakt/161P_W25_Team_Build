from validate import get_valid_choice

def explore_forest(path):
    print ()
    print ("you walk into the "+ path + " and encounter a wild animal!")
    print ("Do you fight, run or try to negotiate?")
    valid_choices = "run fight negotiate"
    choice = get_valid_choice(valid_choices)

    string = ""
    if "fight" in choice:
        string = "You fight bravely in th " + path + " and win the battle!"
    elif "run" in choice:
        string = "You run away safely from the "  + path + " but the adventure ends here"
    elif "negotiate" in choice:
        string = "You successfully negotiate with the wild animal and continue your journey!"

    #print(f"string is {string}")
    return string


