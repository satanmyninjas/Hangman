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
