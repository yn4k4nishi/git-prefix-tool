#coding : utf-8
#!/usr/bin/env python3
import curses
from add import add
from commit import commit
from push import push

def main(stdscr):
    add(stdscr) 
    commit(stdscr)
    push(stdscr)

curses.wrapper(main)
