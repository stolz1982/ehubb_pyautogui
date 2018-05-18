#Instructions to download pyautogui
#pip3 install python3-xlib
#sudo apt-get install scrot
#sudo apt-get install python3-tk
#sudo apt-get install python3-dev
#pip3 install pyautogui

#https://www.youtube.com/watch?v=1RE5tSPO2RI
import pyautogui as pag
import time
#finds the current position
time.sleep(5)
#print(pag.position())


#in order to start the script from this pos 
#python3 pag.py
#Select Product in the upper right corner
pag.click(590,339)
time.sleep(2)
#Press Payment
pag.click(179,654)
time.sleep(2)
#Press Cash
pag.click(233,342)
time.sleep(2)

#1000 entering as tendered
pag.typewrite("1")
time.sleep(1)
pag.typewrite("0")
time.sleep(1)
pag.typewrite("0")
time.sleep(1)
pag.typewrite("0")
time.sleep(1)

#press validate
pag.click(957,181)
time.sleep(2)

#press Next Order
pag.click(957,181)
time.sleep(2)
