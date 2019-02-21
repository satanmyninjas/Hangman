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
