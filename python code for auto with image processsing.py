import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab,ImageOps
from PIL import Image
import time
import pyautogui
import serial
ser=serial.Serial('COM6',baudrate = 9600,timeout=1)

time.sleep(3)
while True:
#img = np.array(ImageGrab.grab(bbox=(940,435,978,470)))

    arduinoData=ser.readline() #.decode('ascii')
    
    print(str(arduinoData))
    
    if  arduinoData == b'1\r\n':                 
        print("checked")
        pyautogui.press('space')
              
    img = np.array(ImageGrab.grab(bbox=(800,400,1100,500)))

    cv2.imwrite("E:\in_memory_to_disk.png", img)

    img=cv2.imread('E:\in_memory_to_disk.png')

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    template=cv2.imread('E:\sorce2.png',0)
    w,h=template.shape[::-1]
    res=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

    threshold=0.8
    loc=np.where(res >=threshold)
    flag = False
    if np.amax(res) > threshold:
        flag = True
        print("true")
        pyautogui.press('space') 
    else:
        print("false")

    time.sleep(0.3)

cv2.waitKey(0)
cv2.destroyAllWindows()
