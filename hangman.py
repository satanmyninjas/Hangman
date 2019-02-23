import random


"""
Add game logic for later on, reuse older code
i.e chomp
begin on game logic for now,
refresh on using csv files and how
to use them, read documentation + notes
from class

remind:
from hangman import hang
from <file name> import <function / class / whatever>
"""


# note: does not have empty gallows at start, begins at head.
def hang():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    # double loop below allows for this enum index-value pair
    # to simply get the next piece
    for i, v in enumerate(sequence, start=1):
        # enumerate(sequence) creates tuples + iterator, thus
        # getting the index-value pairs
        for k in range(v):
            gallows[i] += next(parts)
            yield '\n'.join(gallows)
            # adds, then joins together
    raise StopIteration
# unchanging, keep constant. no touchy


# randomly selecting a word
# TODO: fix this hot mess
def choose_word():
    with open('words.csv') as csv_file:
        words = list(csv_file)
        word_list = [word[:-1] for word in words if word == word.lower()
                     and len(word) > 4
                     and "-" not in word
                     and "'" not in word]
        yield random.choices(word_list)


# other functions are defined above to be used down here for reference
mistakes = 0  # once 8 repetitions of hang() is done, game over
secret = choose_word()
underscores = ["_ " for letter in secret]
tries_left = int((8 - mistakes))
lynch = hang()
correct_guesses = 0  # will go up if you guess correctly, if win_count == len(secret_word), you win
game_over = False

# while statement where game is actually ran.
# other functions are defined above to be used down here for reference
while not game_over:
    f'HANGMAN \n'
    print(underscores)
    guess = input("Enter a letter: ")

    if guess in secret:
        correct_guesses += 1
        for letters in secret:
            # keeps track of position, allowing us to redefine our progress as a guess
            for idx, letter in enumerate(secret):  # if given an iterable, enumerate creates index-value pairs
                if letter == guess:
                    underscores[idx] = guess
        f'Correct! Keep going. '

    elif guess not in secret:
        mistakes += 1
        print(next(lynch))
        f'Incorrect. So far, you have {tries_left} remaining chances. '

    elif correct_guesses == len(secret) or mistakes == 8:
        f'Number of mistakes made: {mistakes} \n'
        f'Number of times you guessed correctly: {correct_guesses}\n'
        f'The secret word was: {secret}'
        play_again = input("Would you like to stop playing? y / n \n").lower()
        if play_again == "n":
            break


# TODO: guess a letter
# TODO: if guess is incorrect, call hang() and  mistakes += 1
# TODO: if guess is correct, continue on

# TODO: keep checking if the guess matches the word
# TODO: once mistakes = 8, game over

# TODO: give option to play again, y / n
# TODO: if yes, go back to prompting for word length / difficulty for new word
# TODO: if no, break

# look up csv docs

# TODO: for every letter, **try to replace w/ underscores
# TODO: guess
# TODO: if guess is incorrect, call hang() and  mistakes += 1
# TODO: if guess is correct, continue on

# TODO: keep checking if the guess matches the word
# TODO: once mistakes = 8, game over

# TODO: give option to play again, y / n
# TODO: if yes, go back to prompting for word length / difficulty for new word
# TODO: if no, break

# (optional) add a default mode for **any word in the file if player doesn't specify a length

