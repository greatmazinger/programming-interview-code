from basegameengine import BaseGameEngine
from random import randint

class GuessNumEngine(BaseGameEngine):
    def __init__(self, maximum = 100):
        assert(maximum  > 1)
        assert(isinstance(maximum, int))
        print("Guess the number game!")
        self._min = 1 # smallest possible number
        self._max = maximum # largest possible number
        self._secret = randint(1, maximum) # The Secret
        self._guesses = 0 # Number of guesses so far
        self._current_guess = None
        self._num_guesses_allowed = 10
        print("I am thinking of a number between 1 and %d (inclusive)." % maximum)
        print("You have %d guesses to get it right!" % self._num_guesses_allowed)

    def display_game_status(self):
        """Displays the game status for the player."""
        print("======[ This is guess # %d ]=======================================================" % self._guesses)
        if self._guesses > 1:
            assert(self._current_guess != self._secret)
            if self._current_guess > self._secret:
                print("Your last guess was too high!")
            else:
                print("Your last guess was too low!")

    def get_player_move(self):
        """Returns player's next guess."""
        while True:
            guess = input("Enter your guess:")
            try:
                num = int(guess)
                if num > 0:
                    return num
                else:
                    print("Guess should be positive! Try again.")
            except:
                print("%s is not a number! Try again." % guess)

    def check_loop_status(self):
        """Returns True if game should continue:
                * if player guess IS NOT correct. AND
                * number of guesses is still less than maximum allowed.
           Otherwise returns False.
        """
        return (self._secret != self._current_guess) and (self._guesses <= self._num_guesses_allowed)

    def event_loop( self ):
        self._guesses += 1
        while self.check_loop_status():
            self.display_game_status()
            self._current_guess = self.get_player_move()
            self._guesses += 1
        self.check_game_status()

    def check_game_status(self):
        if ((self._current_guess == self._secret) and
            (self._guesses <= self._num_guesses_allowed)):
            print("You win!")
        else:
            print("Sorry! You lose.")
       

def run():
    engine = GuessNumEngine()
    engine.event_loop()

if __name__ == "__main__":
    run()
