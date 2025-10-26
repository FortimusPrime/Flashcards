# This is the main program that fills the files. The directory must be changed. 

def add_to_file(dir, data1, data2):
    file = open(dir, "a")
    text = data1 + "| " + data2
    file.write(text)
    # file.close()

def main():
    while (True):
        data1 = input("Type the German Word: ")
        data2 = input("Type the English Equivalent: ")
        file = open("../Flash_Card_Content/Chapter 2/6 Question Words/content.txt", "a")
        text = data1 + "| " + data2 + "\n"
        file.write(text)
        
# main()