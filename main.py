from intro import introduction
from play import play_game
from replay import play_again


# def introduction(prompt = "Hi user_name, would you like to play a game y/n?"):
#     valid_input = False
#     show_intro = False
#     while not valid_input:
#         play= input(prompt)
#         if play == "y":
#             show_intro = True
#
#
#     introduction()
#
#
#     print("Let's begin")
#
#
# def playAgain(prompt="Do you want to play again y/n? "):
#    valid_response = False
#    play_again = False
#    while not valid_response:
#       again = input(prompt).strip().lower()
#       if again == 'y':
#         print("Yay! Lets play again.")
#         play_again = True
#         valid_response = True
#       elif again == 'n':
#         print("Thanks for playing!")
#         play_again = False
#         valid_response = True
#       else:
#         print("Invalid input. Please enter 'y' for yes or 'n' for no.")
#    return play_again

def main():
    name = input("Enter your name: ")
    keep_playing = introduction(name)
    while keep_playing:
        play_game()
        keep_playing = play_again()

    print("Thanks for playing the Adventure Game!")


if __name__ == "__main__":
    main()


"""
    Manages the main loop of the Adventure Game, coordinating the game's flow
    from introduction to repeated gameplay sessions.

    Args: None
    Returns: None

    Set name to what they user enters when you ask "Enter your name: "
    Set keep_playing to what introduction returns when you send it name

    As long as keep_playing is True, call play_game and set keep_playing to what play_again returns
    Display "Thanks for playing the Adventure Game!"

    """




