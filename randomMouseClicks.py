import sys
import pyautogui
from random import randint

# Set up (e.g. 2.5) second pause after each PyAutoGUI call
pyautogui.PAUSE = randint(1, 3)

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size() 
print("Screen Resolution")
print(f"width = {screenWidth}, height = {screenHeight}")

try:
    while True:
        num_seconds = randint(0, 7)
        num_of_clicks = randint(0, 3)
        secs_between_clicks = randint(0, 5)
        
        moveX = randint(650, 950)
        moveY = randint(150, 350)
        
        clickX = randint(650, 950)
        clickY = randint(150, 350)

        # Get the XY position of the mouse.
        currentMouseX, currentMouseY = pyautogui.position() 
        print("Current Mouse Position")
        print(f"x = {currentMouseX}, y = {currentMouseY}")

        # Move the mouse to XY coordinates.
        pyautogui.moveTo(moveX, moveY, duration = num_seconds)  

        # Move the mouse to XY coordinates and click it.
        print("Clicking_________________________________________")
        pyautogui.click(clickX, clickY, clicks = num_of_clicks, interval = secs_between_clicks, button = 'left') 
        
        #Positive scrolling will scroll up, negative scrolling will scroll down
        #print("Scrolling Up n Down_________________________________________")
        # amount_to_scroll = randint(0, 5)
        # # moveToX = randint(650, 950)
        # # moveToY = randint(150, 350)
        # # pyautogui.scroll(amount_to_scroll, x = moveToX, y = moveToY)
        # pyautogui.scroll(amount_to_scroll)
        # pyautogui.scroll(-amount_to_scroll)
        

except KeyboardInterrupt:
    print ("Exiting PyAutoGUI")
    sys.exit()
    