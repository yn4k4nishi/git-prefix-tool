import curses, yaml

def load_temp(file_path):
    with open(file_path, 'r') as yml:
        temp = yaml.load(yml, Loader=yaml.SafeLoader)
        return temp
    
def select_temp(stdscr):
    temp = load_temp('/opt/git-prefix-tool/template.yaml')
    max_len_prefix = max([len(y) for y in [i.get('prefix') for i in temp['prefix']]])

    cursor = 1

    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, -1, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)

    while True:
        stdscr.clear()
        stdscr.keypad(True) 

        stdscr.addstr(0,0,"Select Prefix List Below.", curses.color_pair(2))

        i = 1
        for t in temp['prefix']:
            try:
                if(i == cursor):
                    stdscr.addstr(i, 0, "> " + t['prefix'] + " "*(max_len_prefix - len(t['prefix'])), curses.color_pair(1))
                    stdscr.addstr(i, max_len_prefix + 2, " : " + t['ditail']                        , curses.color_pair(1))
                else:
                    stdscr.addstr(i, 0, "  " + t['prefix'])
                    stdscr.addstr(i, max_len_prefix + 2,  " : " + t['ditail'])    
            except curses.error:
                pass

            i += 1

        stdscr.refresh()
        key = stdscr.getkey()

        if len(key) == 1 and ord(key) == 27: # ESC
            quit()
        elif key == 'KEY_UP':
            cursor += -1
            cursor = max(cursor, 1)
        elif key == 'KEY_DOWN':
            cursor += 1
            cursor = min(cursor, len(temp['prefix']))
        elif key == '\n':
            return temp['prefix'][cursor-1]['emoji'] +  " " + temp['prefix'][cursor-1]['prefix']

        

if __name__ == "__main__":
    curses.wrapper(select_temp)
