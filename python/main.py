#coding : utf-8
#!/usr/bin/env python3
import curses
from add import add
from commit import commit

def main(stdscr):
    add(stdscr)
    commit(stdscr)

curses.wrapper(main)

