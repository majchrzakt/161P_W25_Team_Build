from validate import get_valid_choice
valid_choices = ["run", "fight", "negotiate"]
def explore_forest(path):
    print ()
    print ("you walk into the "+ (path) + " and encounter a wild animal!")
    choice = input ("Do you fight, run or try to negotiate?")

    if choice in valid_choices:
        if choice == "fight":
            string = "You fight bravely in th " + (path) + " and win the battle!"
        elif choice == "run":
            string = "You run away safely from the"  + (path) +"but the adventure ends here"

        else:
            string = "You successfully negotiate with the wild animal and continue your journey!"

    return string



