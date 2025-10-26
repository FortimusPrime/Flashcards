import curses
import os

def read_folders(path):
    folders = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            folders.append(entry)
    folders.sort()
    return folders

def read_contents(path):
    contents = os.listdir(path)
    contents.sort()
    for item in contents:
        if item.startswith("."):
            contents.remove(item)
    # contents.remove(".DS_Store")
    return contents

from content_selection import display_content_selection_screen
from chapter_contents import chapter_contents
from flashcards import flashcards_init

def main(stdscr):
    height, width = stdscr.getmaxyx() # Get height and width of working screen.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
    stdscr.bkgd(' ', curses.color_pair(1))                     # apply white background
    centerText = "Welcome to German Flashcards!"
    stdscr.clear()
    stdscr.addstr(height//2, width//2 - len(centerText)//2, centerText, curses.color_pair(1)) # Print first text. 
    stdscr.refresh()
    stdscr.getch()
    while(True):
        chapterContent = read_folders("../Flash_Card_Content")
        # chapterContent = ["Chapter 1", "Chapter 2", "Chapter 3"] # Adjust as desired. 

        # This selects the chapter to use. 
        chapterSelection = display_content_selection_screen(stdscr, chapterContent, "Select the Chapter to Review:")

        # This function gathers the data of the selected chapter for displaying on the next line. 
        # fileContent = chapter_contents(chapterSelection)

        contentDir = "../Flash_Card_Content" + "/" + chapterContent[chapterSelection]
        fileContent = read_contents(contentDir)

        # This displays the content on the 
        if len(fileContent) != 0:
            folderSelection = display_content_selection_screen(stdscr, fileContent, "Select the Content to Review:")
            reviewDir = contentDir + "/" + fileContent[folderSelection] + "/" + "review.txt"
            dir = contentDir + "/" + fileContent[folderSelection] + "/" +"content.txt"

            # This function uses the chapter selection and folder selection to navigate to the data and parse it to display it. 
            flashcards_init(stdscr, chapterSelection, folderSelection, dir, reviewDir)
        else:
            centerText = "No content available in this folder."
            stdscr.clear()
            stdscr.addstr(height//2, width//2 - len(centerText)//2, centerText, curses.color_pair(1)) # Print first text. 
            stdscr.refresh()
            stdscr.getch()
curses.wrapper(main)