#coding : utf-8
#!/usr/bin/env python3
import curses
from commit import commit

def main(stdscr):
    commit(stdscr)
        
curses.wrapper(main)
