import os

def read_chapter_folders():
    folder_path = "../Flash_Card_Content"   # current directory
    contents = os.listdir(folder_path)
    return contents

# NOTE TO SELF: Must make a function to read the folders to dynamically make this work. 
def chapter_contents(chapterSelection):
    if chapterSelection == 1:
        contents = []
    elif chapterSelection == 2:
        contents = ["Nouns", "Verbs", "Adjectives", "Other"]
    elif chapterSelection == 3:
        contents = []
    return contents
