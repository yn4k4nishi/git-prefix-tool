import curses
import os
import subprocess


def add(stdscr):

    cursor = 1

    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, -1, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)

    not_staged = ["[Select ALL]"]

    cmd = 'git ls-files --others --exclude-standard'
    tmp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    tmp = tmp.communicate()[0]
    not_staged += tmp.decode('utf-8').split('\n')[:-1]

    cmd = 'git diff --name-only'
    tmp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    tmp = tmp.communicate()[0]
    not_staged += tmp.decode('utf-8').split('\n')[:-1]

    selected = [True] * len(not_staged)

    if len(not_staged) == 1:
        stdscr.clear()
        stdscr.keypad(True)

        msg = "Cannot find Changes. Pless some key to finish."
        stdscr.addstr(0, 0, msg, curses.color_pair(2))

        stdscr.refresh()
        stdscr.getkey()
        quit()

    while True:
        stdscr.clear()
        stdscr.keypad(True)

        msg = "Select Add Files (pless SPACE Key to check)."
        stdscr.addstr(0, 0, msg, curses.color_pair(2))

        if selected[0]:
            selected = [True] * len(not_staged)

        i = 1
        for u in not_staged:

            text = "  " + u
            if selected[i-1]:
                text = "✅ " + u

            try:
                if(i == cursor):
                    stdscr.addstr(i, 2, text, curses.color_pair(1))
                else:
                    stdscr.addstr(i, 2, text)
            except curses.error:
                pass

            i += 1

        # stdscr.addstr(i+1, 0, "Pless Enter to go next", curses.color_pair(2))

        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27:  # ESC
            quit()
        elif key == 'KEY_UP':
            cursor += -1
            cursor = max(cursor, 1)
        elif key == 'KEY_DOWN':
            cursor += 1
            cursor = min(cursor, len(not_staged))
        elif key == ' ':
            selected[cursor-1] = not selected[cursor-1]
            if cursor != 1:
                selected[0] = False
        elif key == '\n':
            if not any(selected):
                pass
            elif selected[0]:
                os.system('git add .')
                break
            else:
                for i in range(len(not_staged)):
                    if selected[i]:
                        os.system('git add ' + not_staged[i])
                break


if __name__ == "__main__":
    curses.wrapper(add)
