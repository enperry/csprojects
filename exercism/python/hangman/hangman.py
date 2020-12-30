STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:

    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.game = ["_" for i in self.word]

    def guess(self, char):
        if(self.status != STATUS_ONGOING):
            raise ValueError("game over")
        if(char not in self.word or char in self.game):
            self.remaining_guesses = self.remaining_guesses - 1
        else:
            for i, n in enumerate(self.word):
                if(n == char):
                    self.game[i] = char

    def get_masked_word(self):
        return "".join(self.game)

    def get_status(self):
        if(self.get_masked_word() == self.word):
            self.status = STATUS_WIN
        elif(self.remaining_guesses < 0):
            self.status = STATUS_LOSE
        return self.status