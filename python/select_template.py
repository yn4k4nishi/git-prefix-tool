import curses
import yaml


def load_temp(file_path):
    with open(file_path, 'r') as yml:
        temp = yaml.load(yml, Loader=yaml.SafeLoader)
        return temp


def select_temp(stdscr):
    temp = load_temp('/opt/git-prefix-tool/template.yaml')
    prefix_list = [i.get('prefix') for i in temp['prefix']]
    max_len_prefix = max([len(y) for y in prefix_list])

    cursor = 1

    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, -1, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)

    while True:
        stdscr.clear()
        stdscr.keypad(True)

        msg = "Select Prefix List Below."
        stdscr.addstr(0, 0, msg, curses.color_pair(2))

        i = 1
        for t in temp['prefix']:
            try:
                if(i == cursor):
                    msg = ">>" + t['emoji'] + "  "
                    stdscr.addstr(i, 0, msg, curses.color_pair(1))
                    msg = t['prefix'] + " "*(max_len_prefix + 3 - len(t['prefix']))
                    stdscr.addstr(i, 6, msg, curses.color_pair(1))
                    msg = " : " + t['ditail']
                    stdscr.addstr(i, max_len_prefix+8, msg, curses.color_pair(1))
                else:
                    stdscr.addstr(i, 0, "  " + t['emoji'])
                    stdscr.addstr(i, 6, t['prefix'])
                    stdscr.addstr(i, max_len_prefix + 8, " : " + t['ditail'])
            except curses.error:
                pass

            i += 1

        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27:  # ESC
            quit()
        elif key == 'KEY_UP':
            cursor += -1
            cursor = max(cursor, 1)
        elif key == 'KEY_DOWN':
            cursor += 1
            cursor = min(cursor, len(temp['prefix']))
        elif key == '\n':
            r = temp['prefix'][cursor-1]['emoji_code']
            r += " " + temp['prefix'][cursor-1]['prefix']
            return r


if __name__ == "__main__":
    curses.wrapper(select_temp)
