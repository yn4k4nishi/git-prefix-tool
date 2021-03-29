#coding : utf-8
#!/usr/bin/env python3
import os, curses
from select_template import select_temp

def main(stdscr):
    if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
    
    temp = select_temp(stdscr)

    body = ""
    while True:
        stdscr.clear()
        stdscr.keypad(True) 
        curses.use_default_colors()
        curses.init_pair(2, curses.COLOR_CYAN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)

        stdscr.addstr(0, 0, temp, curses.color_pair(2))
        stdscr.addstr(1, 0, "Write Body", curses.color_pair(3))
        stdscr.addstr(2, 2, body)
        
        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27: # ESC
            break
        elif key == '\n':
            break
        elif key == 'KEY_BACKSPACE':
            body = body[:-1]
        else:
            body += key
        

os.environ['TERM'] = 'xterm-256color'
curses.wrapper(main)