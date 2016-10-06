import curses, os, sys

if len(sys.argv) is 1 and os.path.isfile('input.txt.hacker'):
    src_file = open('input.txt.hacker')
elif len(sys.argv) is 2 and os.path.isfile(sys.argv[1]):
    src_file = open(sys.argv[1])
else:
    print("Either have a file called 'input.txt.hacker' or supply a file "
    "name as the first argument, e.g. python main.py test.py")
    exit(1)

myscreen = curses.initscr()
curses.start_color()
curses.noecho()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
char = 0

myscreen.getch()

for line in src_file:
    if char == 27:
        break


    for word in line:
        myscreen.addstr(word , curses.color_pair(1))
        myscreen.refresh()
        char = myscreen.getch()
        if char == 27:
            break

    myscreen.refresh()

if char == 27:
    curses.endwin()
else:
    while char != 27:
        char = myscreen.getch()

    curses.endwin()
