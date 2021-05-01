from random import choice
from string import ascii_lowercase


class Hangman:
    guessed = set()

    def __init__(self, words, guess):
        self.words = words
        self.guess = guess

    def chech(self, word):
        if len(word) != 1:
            print('Please input a single letter!')
            return
        if word not in ascii_lowercase:
            print('Please enter a lowercase letter!')
            return
        if word in self.guessed:
            print('You have already guessed this letter')
            return
        return True

    def reset(self):
        self.guessed = set()
        word = choice(self.words)
        return word, ['-'] * len(word), self.guess

    def play(self):
        word, hidden, lives = self.reset()

        while lives > 0:
            print(''.join(hidden))
            entry = input('Please enter a letter: ')
            if self.chech(entry):
                self.guessed.add(entry)
                if entry in word:
                    for i in range(len(word)):
                        if entry == word[i]:
                            hidden[i] = entry
                else:
                    print('Your guess is not correct.')
                    lives -= 1
            if '-' not in hidden:
                break

        print('You guessed the word!' if '-' not in hidden else 'You lost!')

    def main(self):
        while True:
            entry = input('Type "play" to play the game, "exit" to quit: ')
            if entry == 'play':
                self.play()
            if entry == 'exit':
                break


words = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
game = Hangman(words, 3)
game.main()
