"""
Add game logic for later on, reuse older code
i.e chomp

Will use other solution (as this one
clearly doesn't work well)

begin on game logic for now,
refresh on using csv files and how
to use them, read documentation + notes
from class
"""

# just void this bs attempt in the meantime

def hangman_gen():
# what i'm basing the list off
  pieces = ["", "0", "/", "|", "\ ", "^", "/", " \ ", "°", "   °"]

  structure = [
               "|--------|",
               "|        ",
               "|       ",
               "|        ",
               "|       ",
               "|      ",
               "|",
               "-----"
               ]

  mistakes = 0
  # look over fibonacci generator for specific usage on other variables

  game_over_trigger = 9
  # trigger game over at this number

  # '\n '.join(structure)
  # structure[1] + pieces[1]
  # while statement below

  while mistakes < game_over_trigger:
      yield mistakes
      mistakes =+ 1
      structure[mistakes] + pieces[mistakes]

      if mistakes == game_over_trigger:
          f'GAME OVER! You made {mistakes} mistakes.'

  for i in structure:
      print(i)
