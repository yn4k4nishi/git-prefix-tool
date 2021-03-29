#!/usr/bin/env python3

import os, curses
def main(stdscr):
    if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
    
    input = "Hello."
    while True:
        stdscr.clear()
        stdscr.keypad(True) 
        curses.use_default_colors()

        stdscr.addstr(1,0,input)
        
        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27: # ESC
            break
        elif key == 'KEY_BACKSPACE':
            input = input[:-1]
        else:
            input += key

os.environ['TERM'] = 'xterm-256color'
curses.wrapper(main)