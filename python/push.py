import curses
import os
import subprocess as subp


def push(stdscr):
    stdscr.clear()
    stdscr.keypad(True)
    curses.use_default_colors()
    curses.init_pair(2, curses.COLOR_YELLOW, -1)

    input = ''
    while True:
        stdscr.clear()
        stdscr.keypad(True)

        msg = "Do you push it ? (Y/n) : "
        stdscr.addstr(0, 0, msg + input, curses.color_pair(2))

        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27:  # ESC
            quit()
        elif key == '\n':
            if(input == 'y' or input == 'Y' or input == ''):
                # stdscr.move(2, 0)
                # os.system('git push -q')
                break
            elif (input == 'n' or input == 'N'):
                break
        elif key == 'y' or key == 'Y':
            input = key
        elif key == 'n' or key == 'N':
            input = key
        elif key == 'KEY_BACKSPACE':
            input = ''

    if(input == 'y' or input == 'Y' or input == ''):
        res = subp.run('git push', shell=True, stdout=subp.PIPE, text=True)
        stdscr.addstr(0, 0, res.stdout)
        stdscr.refresh()
        stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(push)
