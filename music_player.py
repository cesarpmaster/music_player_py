# CLI(command line interface) for the music player
# Authored by: Cesar Perez Vuelvas (checharperezv@gmail.com)

import sys

valid_commands = ["play"]

valid_files = ['Ameno.mp3','Dorime.mp3','Escandalo.mp3','la_tusa.mp3']

try:
  command = sys.argv[1]
except IndexError:
  raise ValueError('Command not supplied')

if command not in valid_commands:
  raise ValueError('Invalid command')

arguments = sys.argv[2:]


if arguments:
  for argument in arguments:
    if argument in valid_files:
        print(f'Playing', argument)
    else:
        print(f"can't be found or accessed{argument}")
else:
  raise ValueError('Play command requires at least one argument')