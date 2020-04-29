# CLI(command line interface) for the music player
# Authored by: Cesar Perez Vuelvas (checharperezv@gmail.com)

import sys

valid_commands = ["play"]

try:
  command = sys.argv[1]
except IndexError:
  raise ValueError('Command not supplied')

if command not in valid_commands:
  raise ValueError('Invalid command')

arguments = sys.argv[2:]

if arguments:
  for argument in arguments:
    print(f'Playing', argument)
else:
  raise ValueError('Play command requires at least one argument')