import pyautogui as pag
import time


def keystroke_mouse(p, x, y, t):
#x and y are the coordinate
#p is the delay before sending the click
#t is the delay in seconds after sending the click
    print p
    print x
    print y
    print t
    time.sleep(p)
    pag.click(x, y)
    time.sleep(t)


def keystroke_keys(p, chars, t, i):
    #chars are the characters to send
    #p is the delay before sending the click
    #t is the delay in seconds after sending the click
    #i is the interval between the characters
    time.sleep(p)
    pag.typewrite(chars, i)
    time.sleep(t)
