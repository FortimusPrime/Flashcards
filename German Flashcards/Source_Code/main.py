import curses
import os

from content_selection import display_content_selection_screen
from chapter_contents import chapter_contents
from flashcards import flashcards_init

# read_folders returns a list of the folders on the specified level. 
def read_folders(path):
    folders = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            folders.append(entry)
    folders.sort()
    return folders


# read_contents returns a list of all the items on the specified level. 
def read_contents(path):
    contents = os.listdir(path)
    contents.sort()
    for item in contents:
        if item.startswith("."): # To remove .DS_store from MacOS systems. 
            contents.remove(item)
    return contents

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
        # Reads the content of the folders at the level of the specified directory. 
        chapterContent = read_folders("../Flash_Card_Content")

        # This selects the chapter to use. 
        chapterSelection = display_content_selection_screen(stdscr, chapterContent, "Select the Chapter to Review:")

        # Navigate to the next page by using the item selected from the chapterContent list, and read items in that directory. 
        contentDir = "../Flash_Card_Content" + "/" + chapterContent[chapterSelection]
        fileContent = read_contents(contentDir)

        # This displays the content on the directory selected. If there is content, it is displayed, otherwise, a message is presented. 
        if len(fileContent) != 0:
            folderSelection = display_content_selection_screen(stdscr, fileContent, "Select the Content to Review:")
            reviewDir = contentDir + "/" + fileContent[folderSelection] + "/" + "review.txt" # Content to review. 
            dir = contentDir + "/" + fileContent[folderSelection] + "/" +"content.txt" # Standard content. 

            # This function uses the chapter selection and folder selection to navigate to the data and parse it to display it. 
            flashcards_init(stdscr, chapterSelection, folderSelection, dir, reviewDir)
        else:
            centerText = "No content available in this folder."
            stdscr.clear()
            stdscr.addstr(height//2, width//2 - len(centerText)//2, centerText, curses.color_pair(1)) 
            stdscr.refresh()
            stdscr.getch()
curses.wrapper(main)