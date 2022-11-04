import curses
from curses import wrapper
import time
import queue

mazze = [
    ["", "#", "#", "#", "#", "#", "o", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " "],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " #", " ", " #", " ", " #",],
    ["#", " ", "#", " ", " #", " ", " #", " ", " #",],
    ["#", " ", "#", " ", " #", " ", " #", "#", " #",],
    ["#", " ", " ", " ", " #", " ", " #", " ", " #",],
     ["#", "#", "#", "#", " #", "#", " #", "X", " #",],

]

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)

    stdscr.clear() #  clear the entire screen
    stdscr.addstr(5, 0, "world!")
    stdscr.refresh() #  fresh the screen
    stdscr.getch()

wrapper(main) #  initailized the cursor module
    