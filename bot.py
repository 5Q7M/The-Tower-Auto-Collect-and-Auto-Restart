import pyautogui
import time

def imagecheck(image, conf=.7, region=None):
    try:
        if region:
            location = pyautogui.locateOnScreen(image, confidence=conf, region=region)
        else:
            location = pyautogui.locateOnScreen(image, confidence=conf)
        
        if location is not None:
            center = pyautogui.center(location)
            return center
             
        else:
            return None
            
    except Exception:
        return None
    
def clickimage(image, conf=.7, region=None):
    if region is not None:
        location = imagecheck(image, conf, region)
    else:
        location = imagecheck(image, conf)
    
    if location is not None:
        pyautogui.click(location)
        
print("Started. ;)")

while True:
    time.sleep(2)
    clickimage("gem.png")
    clickimage("retry.png")
    if imagecheck("dollarsign.png"):
        clickimage("floatgem.png", .5, region=(990,120,300,300))

