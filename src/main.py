import os
import keyboard

def terminate(foo, bar, baz):
    os._exit(0)

keyboard.add_hotkey('ctrl+shift+x', terminate, args=('bar'))

while True:
    pass