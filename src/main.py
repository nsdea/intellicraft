import os
import keyboard

def terminate(foo, bar, baz):
    os._exit(0)

def add_quit_hotkey():
    keyboard.add_hotkey('ctrl+shift+x', terminate, args=('bar'))