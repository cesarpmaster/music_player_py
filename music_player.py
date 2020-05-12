
# CLI(command line interface) for the music player
# Authored by: Cesar Perez Vuelvas (checharperezv@gmail.com)

import sys
import os
from pathlib import Path

valid_commands = ["play"]

places = "C:\\Users\\chech\\music_player_py"

archives = []


try:
  command = sys.argv[1]
except IndexError:
  raise ValueError('Command not supplied')

if command not in valid_commands:
  raise ValueError('Invalid command')

arguments = sys.argv[2:]

if arguments:
  for argument in arguments:
    if os.path.isfile(f"C:\\Users\\chech\\music_player_py\\{argument}"):
      print(f"Playing {argument}")
    else:
        raise ValueError(f"can't be found or accessed{argument}")
else:
  raise ValueError('Play command requires at least one argument')