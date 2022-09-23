import pyautogui
# import win32api, win32con
import time


#Change this variable VVV
subtitleCoordinates = (2531,814)
doneEditingPos = (2231,499)
#Change this variable ^^^

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
            if(pyautogui.pixelMatchesColor(subtitleCoordinates[0], subtitleCoordinates[1], color)):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                mouseDown = True
                count += 1
                print(count)
                if(count == max):
                    time.sleep(1)
                    newContainer()
                    count = 0
               

        else:
            if(not pyautogui.pixelMatchesColor(subtitleCoordinates[0], subtitleCoordinates[1], color, 0)):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                mouseDown = False
        

        
        
def newContainer():
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)
    pyautogui.press("f")
    time.sleep(0.3)
    pyautogui.click(doneEditingPos)
    time.sleep(1)
    pyautogui.press("f")

if __name__ == '__main__':
    main()