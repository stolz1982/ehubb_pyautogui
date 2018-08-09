import keyfunction as func
import random
import time
products = [["Product 1", 574, 300], ["Product 2", 724, 300], ["Product 3", 863, 300]]
buttons = [["payment", 174, 654], ["cash", 335, 266], ["validate", 1115, 176], ["next", 957, 181], ["new_session", 368, 344], ["close_gui", 1250, 123], ["close_db", 430, 358], ["validate", 509, 229], ["continue", 236, 544]]
qty = [["1", 568, 485], ["2", 642, 485], ["3", 717, 485], ["4", 568, 560], ["5", 641, 560], ["6", 715, 560], ["7", 568, 636], ["8", 644, 636], ["9", 715, 636], ["0", 643, 710]]

#start with intial questions
n = 0
a = 0
print('Requirements: maximize your browser window(no fullscreen), ensure that the cash payment is the only one, and cash prefillment is acticated and that the screen is showing the POS Dashboard')
print('How many session the script should create?')
n = int(input())
print('How many times the orders per session should be created?')
r = int(input())
print('How long should take the breaks between the sales?')
b = int(input())


while a < n:
    #start the session
    time.sleep(10)
    print('-------Start Session---------------')    
    print(a)
    #press New Session
    func.keystroke_mouse(1, buttons[4][1], buttons[4][2], 1)
    
    #initial incremental variables
    r = 0
    s = 0
    while s < r:
        # break between the orders
        time.sleep(b)
        print('-------Start Order---------------')
        i = 0
        #sending product(-s) and quantities
        while i < random.randint(1, len(products)):
            n = random.randint(0, len(products) - 1)
            print(products[n][0]) #Product name
            print(products[n][1]) # x
            print(products[n][2]) # y
            #sending the product
            func.keystroke_mouse(2, products[n][1], products[n][2], 1)
            #sending the quantities
            q = random.randint(0, len(qty) - 1)
            func.keystroke_mouse(2, qty[q][1], qty[q][2], 1)
            i = i + 1

        #Pressing payment
        func.keystroke_mouse(1, buttons[0][1], buttons[0][2], 1)

        #Pressing cash
        func.keystroke_mouse(1, buttons[1][1], buttons[1][2], 1)

        #entering the amount of tendered
        #func.keystroke_keys(1, str(random.randint(5000, 7000)), 1, 0.5)

        #Pressing validate
        func.keystroke_mouse(1, buttons[2][1], buttons[2][2], 1)

        #Pressing next
        func.keystroke_mouse(1, buttons[3][1], buttons[3][2], 1)
        
        print('------------Ende Order--------------')
    
    #Press close and confirm quickly at POS GUI Level
    func.keystroke_mouse(1, buttons[5][1], buttons[5][2], 0)
    func.keystroke_mouse(0.2, buttons[5][1], buttons[5][2], 1)
    
    #Press close at POS Dashboard Level
    func.keystroke_mouse(3, buttons[6][1], buttons[6][2], 1)
  
    #Press Validate Closing & Post Entries
    func.keystroke_mouse(3, buttons[6][1], buttons[6][2], 1)
    
    #Press Validate Continue at the deposit check window
    func.keystroke_mouse(3, buttons[7][1], buttons[7][2], 1)
    
print('------------Ende Session--------------')
