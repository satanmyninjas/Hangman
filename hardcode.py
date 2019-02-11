"""
count = 0
game_run = True
def gallows(count):
  """
  'Function defined like so:
  'gallows({number})
  
  'Number has to be 1-9, with 9
  'being when you lose the game.
  """
  a = "  |--------|"
  b = "  |         "
  c = "  |          "
  d = "  |         "
  e = "  |          "
  f = "  |           "
  g = "  |"
  h = "-----"
  if count == 0:
    pass

  if count >= 1:
    b = list(b)
    b[-1] = "O"
    b = ''.join(b)

  if count >= 2:
    c = list(c)
    c[-2] = "|"
    c = ''.join(c)

  if count >= 3:
    c = list(c)
    c[-3] = "/"
    c = ''.join(c)

  if count >= 4:
    c = list(c)
    c[-1] = "\ "
    c = ''.join(c)

  if count >= 5:
    d = list(d)
    d[-1] = "^"
    d = ''.join(d)

  if count >= 6:
    e = list(e)
    e[-3] = "/"
    e = ''.join(e)

  if count >= 7:
    e = list(e)
    e[-1] = "\ "
    e = ''.join(e)

  if count >= 8:
    f = list(f)
    f[-5] = "°"
    f = ''.join(f)

  if count == 9:
    f = list(f)
    f[-1] = "°"
    f = ''.join(f)
    game_run = False

  print(a)
  print(b)
  print(c)
  print(d)
  print(e)
  print(f)
  print(g)
  print(h)
  """
  
  """
  Thinking of implementing classes with specific methods.
  EX: class Hangman
      . . . with all of its sepcific methods.
      
  Should add exception or dialogue
  to occur if the user is a smartass
  and writes in a b.s input.
      
  Or, we can add on to this file and 
  implement the rules of the game 
  into a separate function.
  
  We'll see once we get
  into a flow for this.
  
  - Kayla <3
  """
# adding my own spice to this
def gallows():

  a = "  |--------|"
  b = "  |        " # head
  c = "  |       " # torso, add extra space for last arm
  d = "  |        " # add carrot
  e = "  |       " # add leg, space, leg, space
  f = "  |      " # degree, 3 spaces, degree
  g = "  |"
  h = "-----"

  count = 0

  while True:
    if count == 0:
      pass

    elif count == 1:
      yield b + "0"
      count += 1

    elif count == 2:
      yield c + "/"
      count += 1

    elif count == 3:
      yield c + "|"
      count += 1

    elif count == 4:
      yield c + "\ "
      count += 1

    elif count == 4:
      yield d + "^"
      count += 1

    elif count == 5:
      yield e + "/ "
      count += 1

    elif count == 6:
      yield e + "\ "
      count += 1

    elif count == 7:
      yield f + "°"
      count += 1

    elif count == 8:
      yield f + "   °"
      count += 1
      f'You made {count} mistakes. Game over!'
    
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)
  print(f)
  print(g)
  print(h)
  
def play(letter):
  pass
