import curses
import os 

def push(stdscr):
    stdscr.clear()
    stdscr.keypad(True)
    curses.use_default_colors()
    curses.init_pair(2, curses.COLOR_YELLOW, -1)

    input = ''
    while True:
        stdscr.clear()
        stdscr.keypad(True) 

        stdscr.addstr(0,0,"Do you push it ? (Y/n) : " + input , curses.color_pair(2))
        
        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27: # ESC
            quit()
        elif key == '\n':
            if(input == 'y' or input == 'Y' or input == ''):
                os.system('git push -q')
                break
            elif (input == 'n' or input == 'N'):
                break
        elif key == 'y' or key == 'Y':
            input = key
        elif key == 'n' or key == 'N':
            input = key
        elif key == 'KEY_BACKSPACE':
            input = ''

if __name__ == "__main__":
    curses.wrapper(push)
