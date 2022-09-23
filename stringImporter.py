from pyautogui import *
import win32api, win32con
import time
import ppc as pc

#CHANGE THESE TWO VARIABLES VVV
mousePositionForCopying = (2475,551)
mousePositionForDone = (2224,657)
#CHANGE THESE TWO VARIABLES ^^^

def main():
    userIn = input("Specify the contents of the text file. Enter 'i' for image, 'v' for verticies, 'e' for edges, and 't' for triangles. ")
    if(userIn == 'i'):
        try:
            strings = open("strings","r")
        except:
            input("No text file named 'strings' was found.")

    if(userIn == 'v'):
        try:
            strings = open("verticies","r")
        except:
            input("No text file named 'verticies' was found.")
    
    if(userIn == 'e'):
        try:
            strings = open("edges","r")
        except:
            input("No text file named 'edges' was found.")

    if(userIn == 't'):
        try:
            strings = open("triangles","r")
        except:
            input("No text file named 'triangles' was found.")

    
    print("Strings file found.")
    segments = strings.readlines()
    print("String segments obtained, " + str(len(segments)) + " were found.")
    delay = float(input("Enter a delay timing as a float, should range from 0 to 1 second. "))
    print("Delay set to " + str(delay))
    input("\nPress enter to start the string import process, ensure that the following are true: \n\nThe list create stack that you are importing to is empty. \nYou are seated in the importing seat.  \nYou are holding makerpen in you left hand with the 'wire' tool selected. \nYou are holding the trigger handle in you right hand. \nYou are looking straight on directly above the first list create element.")
    insert(segments,delay)

def insert(list,delay):
    win32api.SetCursorPos((0,0))
    (x,y) = mousePositionForCopying
    (x2,y2) = mousePositionForDone
    for i in enumerate(list):
        (index,string) = i
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        win32api.SetCursorPos((x,y))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        pc.copy(string)
        time.sleep(delay)
        hotkey('ctrl','v')
        time.sleep(delay)
        win32api.SetCursorPos((x2,y2))
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay)
        keyDown('esc')
        keyUp('esc')
        time.sleep(delay)


if __name__ == '__main__':
    main()