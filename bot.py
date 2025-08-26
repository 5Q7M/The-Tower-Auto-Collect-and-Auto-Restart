import pyautogui
import time

def imagecheck(image, conf=.7):
    try:
        location = pyautogui.locateOnScreen(image, confidence=conf)
        
        if location is not None:
            center = pyautogui.center(location)
            return center
             
        else:
            return None
            
    except Exception:
        return None
    
def clickimage(image, conf=.7):
    location = imagecheck(image, conf)
    
    if location is not None:
        pyautogui.click(location)
        
print("Started. ;)")

while True:
    time.sleep(2)
    clickimage("gem.png")
    clickimage("retry.png")

