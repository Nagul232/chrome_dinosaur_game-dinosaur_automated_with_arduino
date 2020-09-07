import serial #import serial for opeing the serial port of arduino to python environment
import pyautogui #for automating keyboard and mouse
import time #time for delay
time.sleep(3)              
ser=serial.Serial('COM6',baudrate = 9600,timeout=1) #this line is for setting up the connection between the arduino and python note:see the com port and baud rate of arduino properly
#class coordinates():                                      
#    replaybtn=(960,450) 
     
while 1:
    arduinoData=ser.readline() #.decode('ascii') #if data from arduino is true it reads and decode the message
    
    #print(str(arduinoData))
    
    if  arduinoData == b'1\r\n':    #if the data is 1 it automatically presses the button                        
        pyautogui.press('space')  #pyautogui function for clicking spacebar
       
