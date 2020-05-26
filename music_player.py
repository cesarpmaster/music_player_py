
# CLI(command line interface) for the music player
# Authored by: Cesar Perez Vuelvas (checharperezv@gmail.com)

import sys
import os
import pyglet
from pathlib import Path

valid_commands = ['play']

archives = []

places = "C:\\Users\\chech\\music_player_py"

window = pyglet.window.Window()

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
    if not Path(argument).exists():
      raise ValueError(f"{argument} can't be found or accessed")
  for argument in arguments:
    print(f'Playing {argument}')
    music = pyglet.resource.media(f'{argument}')
    music.play()
    pyglet.app.run()

  raise ValueError('Play command requires at least one argument')
