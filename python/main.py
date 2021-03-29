#coding : utf-8
#!/usr/bin/env python3
import os, curses
from select_template import select_temp

def main(stdscr):

    prefix = select_temp(stdscr)

    body = ""
    while True:
        stdscr.clear()
        stdscr.keypad(True) 
        curses.curs_set(1)
        curses.use_default_colors()
        curses.init_pair(2, curses.COLOR_CYAN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)

        stdscr.addstr(0, 0, prefix, curses.color_pair(2))
        stdscr.addstr(1, 0, "Write Body and Pless Enter.", curses.color_pair(3))
        stdscr.addstr(2, 2, body)
        
        stdscr.refresh()
        key = stdscr.getkey()

        ## 日本語入力に対応
        if len(key) == 1 and 0xe0 <= ord(key) <= 0xef:
            a = ord(key)
            b = stdscr.getch()
            c = stdscr.getch()
            tmp = map(lambda x: bin(x)[2:], [0b00001111 & a, 0b00111111 & b, 0b00111111 & c])
            tmp = ''.join([item.zfill(6) for item in tmp])
            key = chr(int(tmp,2))

        if len(key) == 1 and ord(key) == 27: # ESC
            break
        elif key == '\n':
            os.system("git commit -m '" + prefix + '\n' + body + "'")
            break
        elif key == 'KEY_BACKSPACE':
            body = body[:-1]
        else:
            body += key
        
curses.wrapper(main)
