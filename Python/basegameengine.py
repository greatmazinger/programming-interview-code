"""
Base class game engine for the the console.

Author: Raoul Veroy

The idea is to have a skeleton base class that implements a basic game loop with:
    * Display game status
    * Get payer input
    * Adjust game conditions
    * Check game status (continue/end/win/lose?)
"""

# Base game engine class for the game
class BaseGameEngine:
    def __init__( self ):
        pass

    # Forms the basic structure of a game.
    #  1. Runs the 'event_loop' until game conditions force an end to the event_loop.
    #  2. 'check_game_status' checks to see if player won, prints out appropriate status
    #      and information.
    def run(self):
        self.event_loop()
        self.check_game_status()

    def check_loop_status(self):
        """Returns True if 'event_loop' should continue. False to exit 'event_loop'"""
        raise RuntimeError("'check_loop_status'must be implemented!")

    # Get the player's next move. Now simply returns the input from the keyboard.
    # This will probably be needed to be reimplemented to suit the game.
    def get_player_move(self):
        """Returns player's next move."""
        return input("Enter your move:")

    def display_game_status(self):
        """Displays the game status for the player."""
        raise RuntimeError("'display_game_status'must be implemented!")

    # Runs a basic event loop as follows:
    # While 'check_loop_status' returns True: loop through the game
    def event_loop( self ):
        while self.check_loop_status():
            self.display_game_status()
            move = self.get_player_move()
        self.check_game_status()

    def check_game_status(self):
        raise RuntimeError("'check_game_status' must be implemented!")
