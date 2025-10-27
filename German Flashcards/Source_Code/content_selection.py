# This is a general function to navigate and select from a list of items on the screen. 

import curses

# Up and down that dynamically adjusts limits according to the length of the content displayed. 
def get_content_selection(key, selection, content):
    if key == curses.KEY_DOWN:
        if selection < len(content) - 1:
            selection += 1
    if key == curses.KEY_UP:
        if selection > 0:
            selection -= 1
    return selection

# Displays arrow on item that is selected. Dynamically adjusts to length of item. 
def display_content(stdscr, selection, content, msgStr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    text = msgStr # + str(selection) # For debugging purposes. 
    stdscr.addstr(height//2 - 5, width//2 - len(text)//2, text)
    i = 0
    while i < len(content): 
        # Iteratively display contents. 
        if i == selection:
            text = "->" + content[i] # Print with arrow if content is selected. 
        else:
            text = "  " + content[i] # So skewing doesn't happen, empty spaces where arrow would be on those that are not the selected value. 
        stdscr.addstr(height//2 + i, width//2 - len(text)//2, text)
        i += 1
    stdscr.refresh()
    
# MAIN FUNCTION. Content is a list that serves as the items that will be displayed. The program automatically adjusts to varying lengths. 
def display_content_selection_screen(stdscr, content, msgStr):
    stdscr.clear()
    selection = 0 # Default selection. 
    while (True): # Infinite loop for interactive display. 
        display_content(stdscr, selection, content, msgStr) # This displays the arrow on the selected item. Displays before adjusting.
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key == 10 or key == 13: # Enter key breaks the loop setting in the selection chosen. 
        # if key == curses.KEY_RIGHT:
            return selection 
        selection = get_content_selection(key, selection, content) # This adjusts the values of the selection depending on the key pressed. 
