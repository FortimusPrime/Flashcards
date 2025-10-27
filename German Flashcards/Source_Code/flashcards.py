import curses
import random
from filler import add_to_file
# shuffle_dict shuffles the key-value pairs. 
def shuffle_dict(data):
    keys = list(data.keys()) # make a list of the keys
    random.shuffle(keys) # shuffle the order of the keys
    new_dict = {} # make a new empty dictionary

    for k in keys: # go through the shuffled keys
        new_dict[k] = data[k] # copy key and its value

    return new_dict

# invert_dict inverses the key-value pairs to value-key pairs.
def invert_dict(data):
    new_dict = {}
    for key in data:
        value = data[key]
        new_dict[value] = key
    return new_dict

# parse_cards reads the file.txt contents and parses between German words and English words by the divisor "|" and returns a dictionary that has the content divided. 
def parse_cards(dir):
    flashcards = {}
    file = open(dir, "r")
    for line in file:
        divisor = line.find("|")
        germanWord = line[:divisor]
        englishWord = line[divisor+1:]
        if germanWord not in flashcards:
            flashcards[germanWord] = englishWord
    return flashcards
    

# # This is the function that selects the directory to parse. NOTE TO SELF, Add automatic navigation
# def fill_flashcards(chapter, stack):
#     dir = None
#     if chapter == 1:
#         return
#     elif chapter == 2:
#         if stack == 1:
#             # Nouns
#             dir = "../Flash_Card_Content/Chapter 2/Nouns/germanNouns.txt"
#         elif stack == 2:
#             # Verbs
#             dir = "../Flash_Card_Content/Chapter 2/Nouns/germanNouns.txt"
#         elif stack == 3:
#             # Adjectives
#             dir = "../Flash_Card_Content/Chapter 2/Nouns/germanNouns.txt"
#         elif stack == 4:
#             # Other
#             dir = "../Flash_Card_Content/Chapter 2/Nouns/germanNouns.txt"
#     elif chapter == 3:
#         return
#     flashcards = parse_cards(dir)
#     return flashcards



def flashcards_init(stdscr, chapter, stack, dir, reviewDir):
    height, width = stdscr.getmaxyx()
    isReviewStack = False

    text = "Review Full Stack or Review Stack?"
    stdscr.addstr(height//2-2, width//2 - len(text)//2, text, curses.color_pair(1))
    # key = stdscr.getch()
    flashcards = parse_cards(dir)
    # if key == curses.KEY_LEFT:
    #     flashcards = parse_cards(reviewDir)
    #     isReviewStack = True

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
    stdscr.bkgd(' ', curses.color_pair(1))                     # apply background color

    centerText = "Flashcards! (Full STACC)"
    if isReviewStack:
        centerText = "Flashcards Review Stack!"

    flashcards = shuffle_dict(flashcards) # Randomize the dictionary.

    # Select where to have cards from German to English, or English to German. 
    num = random.randint(0, 1) 
    if num == 1:
        flashcards = invert_dict(flashcards)

    count = 0
    total = len(flashcards)
    for card in flashcards:
        count += 1
        stdscr.clear()
        stdscr.addstr(height//2-2, width//2 - len(centerText)//2, centerText, curses.color_pair(1))

        countText = str(count) + " of " + str(total)
        stdscr.addstr(height//2, width//2 - len(countText)//2, countText, curses.color_pair(1))

        stdscr.addstr(height//2 + 2, width//2 - len(card)//2, card, curses.color_pair(1))
        stdscr.refresh()

        stdscr.getch() # Press again to reveal card content. 

        stdscr.addstr(height//2 + 5, width//2 - len(flashcards[card])//2, flashcards[card], curses.color_pair(1))
        stdscr.refresh()
        key = stdscr.getch()

        # NOTE: To add review feature later. 
        # if key == curses.KEY_DOWN and not isReviewStack:
        #     add_to_file(reviewDir, card, flashcards[card])
        #     text = "Stored to Review! Press any key to continue."
        #     stdscr.addstr(height//2 + 7, width//2 - len(text)//2, text, curses.color_pair(1))
        #     stdscr.getch()



