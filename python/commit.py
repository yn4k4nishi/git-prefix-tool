#!/usr/bin/env python3
# coding : utf-8

import os
import curses
from select_template import select_temp
import unicodedata as ucd


def commit(stdscr):

    prefix = select_temp(stdscr)

    cursor = 0
    body = ""

    stdscr.keypad(True)
    curses.curs_set(1)
    curses.use_default_colors()
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)

    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, prefix, curses.color_pair(2))
        msg = "Write Body and Pless Enter."
        stdscr.addstr(1, 0, msg, curses.color_pair(3))
        stdscr.addstr(2, 2, body)

        cursor_ = 0
        for i in body[:cursor]:
            if ucd.east_asian_width(i) in 'FWA':
                cursor_ += 2
            else:
                cursor_ += 1

        stdscr.move(2, 2 + cursor_)

        stdscr.refresh()
        key = stdscr.getkey()

        # 日本語入力に対応
        if len(key) == 1 and 0xe0 <= ord(key) <= 0xef:
            a = ord(key)
            b = stdscr.getch()
            c = stdscr.getch()
            tmp = map(lambda x: bin(x)[2:],
                      [0b00001111 & a, 0b00111111 & b, 0b00111111 & c])
            tmp = ''.join([item.zfill(6) for item in tmp])
            key = chr(int(tmp, 2))

        if len(key) == 1 and ord(key) == 27:  # ESC
            quit()
        elif key == '\n':
            os.system("git commit -m '" + prefix + ' : ' + body + "'")
            break
        elif key == 'KEY_BACKSPACE':
            if cursor != 0:
                body = body[:cursor-1] + body[cursor:]
                cursor += -1
        elif key == 'KEY_DC':
            body = body[:cursor] + body[cursor+1:]
        elif key == 'KEY_LEFT':
            cursor += -1
        elif key == 'KEY_RIGHT':
            cursor += 1
        elif len(key) > 1:
            pass
        else:
            body = body[:cursor] + key + body[cursor:]
            cursor += 1

        cursor = min(cursor, len(body))
        cursor = max(cursor, 0)


if __name__ == "__main__":
    curses.wrapper(commit)
