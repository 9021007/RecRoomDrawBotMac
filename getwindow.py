import pywinctl as pwc
import time
import pyautogui
import os
import pd2 as pd
# import mouse

title = input("Enter window title: ")
x = pwc.getWindowsWithTitle(title)[0].left
y = pwc.getWindowsWithTitle(title)[0].top
subtitleCoordinates = (x+511,y+631)
print(x)
print(y)
print(subtitleCoordinates)


def main():
    color = (255,255,255)
    mouseDown = False
    count = 0
    maxTriangles = 336
    maxEdges = 1000

    wireframe = True
    if(wireframe):
        max = maxEdges
    else:
        max = maxTriangles
    while(True):
        if(not mouseDown):
            if(pd.getPixelValues(subtitleCoordinates[0], subtitleCoordinates[1])==color):
                #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                #mouse.press(button='left')
                # os.system("cliclick -m verbose dd:.")
                pyautogui.mouseDown()
                mouseDown = True
                count += 1
                print(count)
                if(count == max):
                    time.sleep(1)
                    newContainer()
                    count = 0
            #    if(pyautogui.pixelMatchesColor(subtitleCoordinates[0], subtitleCoordinates[1], color)):

        else:
            if(not pd.getPixelValues(subtitleCoordinates[0], subtitleCoordinates[1])==color):
                #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                # mouse.release(button='left')
                # os.system("cliclick -m verbose du:.")
                pyautogui.mouseUp()
                mouseDown = False
        
        
def newContainer():
    
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #os.system("cliclick -m verbose du:.")
    pyautogui.mouseUp()
    # mouse.release(button='left')
    time.sleep(0.1)
    # pyautogui.press("f")
    # time.sleep(0.3)
    # pyautogui.click(doneEditingPos)
    # time.sleep(1)
    # pyautogui.press("f")

if __name__ == '__main__':
    main()