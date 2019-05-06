import keyfunction as func
import random
import time
products = [["Product 1", 586, 340], ["Product 2", 719, 340], ["Product 3", 875, 340]]
buttons = [["payment", 170, 973, ["cash", 660, 262], ["validate", 1437, 176], ["next", 1409, 183], ["new_session", , ], ["close_gui", 1891, 125], ["close_db", 426, 376], ["end of session", 1443, 385], ["continue", 555, 546], ["print", 663,244 ], ["print_confirmation", 945, 768]]
qty = [["1", 300, 870], ["2", 350, 870], ["3", 400, 870], ["4", 300, 920], ["5", 350, 920], ["6", 400, 920], ["7", 300, 970], ["8", 350, 970], ["9", 400, 970]]

#start with intial questions
se = 0
a = 0
print('Requirements: maximize your browser window(no fullscreen), ensure that the cash payment is the only one, and cash prefillment is acticated and that the screen is showing the POS Dashboard')
print('How many session the script should create?')
se = int(input())
print('How many times the orders per session should be created?')
r = int(input())
print('How long should take the breaks between the sales?')
b = int(input())


while a < se:
    #start the session
    time.sleep(10)
    print('-------Start Session---------------')    
    print(a)
    #press New Session
    func.keystroke_mouse(1, buttons[4][1], buttons[4][2], 1)
    time.sleep(5)
    
    #initial incremental variables
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

        #Pressing print
        func.keystroke_mouse(1, buttons[9][1], buttons[9][2], 1)
        
         #Pressing OK
        func.keystroke_mouse(3, buttons[10][1], buttons[10][2], 5)
        
        #Pressing next
        func.keystroke_mouse(1, buttons[3][1], buttons[3][2], 1)
        
        print('------------Ende Order--------------')
        s = s + 1
    
    #Press close and confirm quickly at POS GUI Level
    func.keystroke_mouse(1, buttons[5][1], buttons[5][2], 0)
    func.keystroke_mouse(0.2, buttons[5][1], buttons[5][2], 1)
    print('after Press close and confirm quickly at POS GUI Level')
    
    #Press close at POS Dashboard Level
    func.keystroke_mouse(5, buttons[6][1], buttons[6][2], 3)
    print('after Press close at POS Dashboard Level')
    
    #Press Validate Closing & Post Entries
    func.keystroke_mouse(5, buttons[7][1], buttons[7][2], 3)
    print('after Press Validate Closing & Post Entries')
    
    #Press Continue at the deposit check window
    func.keystroke_mouse(5, buttons[8][1], buttons[8][2], 3)
    print('after Press Continue at the deposit check window')
    print('------------Ende Session--------------')
    
    # break between the sessions
    # the break for 250 order will take roughly 100 seconds to get processed
    time.sleep(120)
    a = a + 1
