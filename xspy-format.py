#!/usr/bin/python3
try:
    oldLog = open(argv[1], "r")
except IndexError:
    print("Please supply a file to format.")
    exit()
except FileNotFoundError:
    print("File not found, please enter the filename or location correctly.")
    exit()

def main(oldLog, newLog):
    for line in oldLog:
        while (linearSearch(line, "BackSpace") != "end"): # Remove "Backspace" and one letter before it
            index = linearSearch(line, "BackSpace")-1
            line = line[0:index] + line[index+1:]
            line = line.replace("BackSpace", '', 1)
        line = line.replace("minus", '-') # Replace "minus" with a dash
        line = line.replace("Shift_L backslash", '|') # Replace shift blackslash with pipe
        line = line.replace("backslash", '\\')
        line = line.replace("slash", '/')
        line = line.replace("KP_End", '1')
        line = line.replace("KP_Down", '2')
        line = line.replace("KP_Next", '3')
        line = line.replace("KP_Left", '4')
        line = line.replace("KP_Begin", '5')
        line = line.replace("KP_Right", '6')
        line = line.replace("KP_Home", '7')
        line = line.replace("KP_Up", '8')
        line = line.replace("KP_Prior", '9')
        line = line.replace("KP_Enter", '\n')
    newLog.write(line)

# Searches for characters from a given word in a line of text, and returns index of where it starts
def linearSearch(line, word):
    for i in range(len(line)):
        if line[i:i+len(word)] == word:
            return i
    return "end"

newLog = open("formatted-" + argv[0])
main(oldLog, Newlog)
