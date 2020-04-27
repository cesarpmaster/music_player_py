# CLI(command line interface) for the music player

import sys

try:
    command = sys.argv[1]
except IndexError:
    raise ValueError('Invalid command')

if command != 'play':
    raise ValueError('Invalid command')

arguments = sys.argv[2:]

for argument in arguments:
    print('Playing', argument)
