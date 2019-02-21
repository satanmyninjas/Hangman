import csv
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

# probably unneeded
class Hangman:
  # Innit
  # repr

  # note: does not have empty gallows at start, begins at head
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

  def play():
   mistakes = 0
   while mistakes < 8:
      choose_word(input)
      secret = pass # what the comp chose from the file
      guess = input("Enter a letter: ")
      if guess == secret:
        f'Correct!'
        # replace the blank with what the user guessed
      else:
        pass



  def choose_word(input):
    with open('words.csv', mode='r') as csv_file:
      for character in csv_file:
        print "_ "

    # implement difficulty or word length
    # pick word at random
    # for every letter, **try to replace w/ underscores
    # guess
    # if guess is incorrect, call hang() and  mistakes += 1
    # if guess is correct, continue on

    # keep checking if the guess matches the word
    # once mistakes = 8, game over

    # give option to play again, y / n
    # if yes, go back to prompting for word length / difficulty for new word
    # if no, break

    # add a default mode for **any word in the file if player doesn't specify a length
    # look up csv docs


    # for every letter, **try to replace w/ underscores
    # guess
    # if guess is incorrect, call hang() and  mistakes += 1
    # if guess is correct, continue on

    # keep checking if the guess matches the word
    # once mistakes = 8, game over

    # give option to play again, y / n
    # if yes, go back to prompting for word length / difficulty for new word
    # if no, break

    # add a default mode for **any word in the file if player doesn't specify a length
    # look up csv docs

