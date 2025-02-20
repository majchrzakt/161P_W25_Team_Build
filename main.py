from intro import introduction
from play import play_game
from replay import play_again

def main():
    """
    Manages the main loop of the Adventure Game, coordinating the game's flow
    from introduction to repeated gameplay sessions.

    Args:
        None

    Returns:
        None

    Behavior:
    - Prompts the player to enter their name.
    - Calls the `introduction` function with the player's name to display the game intro
      and determine if the player is ready to begin.
    - If the player is ready (`introduction` returns True), enters a loop where:
        - The `play_game` function is called to execute the main game sequence.
        - After each game session, the `play_again` function is called to ask the player
          if they wish to play another round.
    - The loop continues as long as the player chooses to keep playing.
    - Once the player decides to stop, prints a farewell message thanking them for playing.

    Note:
    - The `introduction` function is expected to handle user input to confirm if the player
      is ready to start the game.
    - The `play_game` function encapsulates the core gameplay mechanics.
    - The `play_again` function prompts the player to decide whether to play another round
      and returns a boolean value accordingly.

    Example:
        >>> main()
        Enter your name: Alice
        Welcome to the Adventure Game, Alice!
        Choose your path and actions wisely!
        Are you ready to begin? (yes/no)
        > yes
        (Game starts...)
        Do you want to play again? (yes/no)
        > no
        Thanks for playing the Adventure Game!

    In this example, the player named Alice starts the game, plays one session, and then
    decides not to play again, upon which the game thanks her for playing.

    References:
    - `introduction` function: Displays the game introduction and checks if the player is ready.
    - `play_game` function: Contains the main gameplay logic.
    - `play_again` function: Asks the player if they wish to play another round.

    """

