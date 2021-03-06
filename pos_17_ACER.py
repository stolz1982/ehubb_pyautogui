import keyfunction as func
import random
import time
products = [["Product 1", 580, 390], ["Product 2", 724, 390], ["Product 3", 866, 390]]
buttons = [["payment", 174, 915], ["cash", 335, 266], ["validate", 1115, 210], ["next", 1100, 210], ["new_session", 368, 390], ["close_gui", 1250, 165], ["close_db", 425, 406], ["validate", 509, 229], ["continue", 236, 570], ["print", 663,244 ], ["print_confirmation", 945, 768],["close_session",1120,410]]
qty = [["1", 300, 820], ["2", 350, 820], ["3", 400, 820], ["4", 300, 870], ["5", 350, 870], ["6", 400, 870], ["7", 300, 920], ["8", 350, 920], ["9", 400, 920], ["0", 350, 970]]

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
#        func.keystroke_mouse(1, buttons[9][1], buttons[9][2], 1)
        
         #Pressing OK
#        func.keystroke_mouse(3, buttons[10][1], buttons[10][2], 5)
        
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
    
    #Press Validate Close Session
    func.keystroke_mouse(5, buttons[11][1], buttons[11][2], 3)
    print('after Press Validate Closing & Post Entries')
    
    #Press Continue at the deposit check window
    func.keystroke_mouse(5, buttons[8][1], buttons[8][2], 3)
    print('after Press Continue at the deposit check window')
    print('------------Ende Session--------------')
    
    # break between the sessions
    # the break for 250 order will take roughly 100 seconds to get processed
    time.sleep(1200)
    a = a + 1
