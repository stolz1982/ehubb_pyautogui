#DELL 2711
import keyfunction as func
import random
import time
products = [["Product 1", 550, 315], ["Product 2", 710, 315], ["Product 3", 870, 315], ["Product 4", 1000, 315], ["Product 5", 1130, 315], ["Product 6", 1280, 315], ["Product 7", 1420, 315], ["Product 8", 1560, 315], ["Product 9", 1700, 315]]
buttons = [["r_payment", 176, 1327], ["r_cash", 979, 263], ["r_validate", 1754, 181], ["r_next_order", 1739, 180], ["R_new_session", 377, 353], ["r_close_gui", 2530, 122], ["r_close_db", 425, 373], ["r_validate", 1751, 179], ["r_continue", 876, 544], ["r_print", 1317,250 ], ["print_confirmation", 945, 768], ["r_end_of_session", 1752, 378]]
qty = [["1", 300, 1230], ["2", 350, 1230], ["3", 400, 1230], ["4", 300, 1280], ["5", 350, 1280], ["6", 400, 1280], ["7", 300, 1340], ["8", 350, 1340], ["9", 400, 1340], ["0", 643, 710]]

#start with intial questions
se = 0
a = 0
print('Requirements: maximize your browser window(no fullscreen) and 100% zoom at a resolution of 2560x1440, ensure that the cash payment is the only one, and cash prefillment is acticated and that the screen is showing the POS Dashboard')
print('How many session the script should create?')
se = int(input())
print('How many orders per session should be created?')
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
        #func.keystroke_mouse(1, buttons[9][1], buttons[9][2], 1)
        
         #Pressing OK
        #func.keystroke_mouse(3, buttons[10][1], buttons[10][2], 5)
        
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
    
    #Press End of Session at POS Dashboard Level
    func.keystroke_mouse(5, buttons[11][1], buttons[11][2], 3)
    print('after Press End of Session at POS Dashboard Level')

    #Press Continue at POS Dashboard Level as Warning if the daily sales have been transfered
    func.keystroke_mouse(5, buttons[8][1], buttons[8][2], 3)
    print('after Press Continue at the Warning POPUP if the daily sales have been transfered')

    print('------------Ende Session--------------')
    
    # break between the sessions
    # the break for 250 order will take roughly 100 seconds to get processed
    time.sleep(120)
a = a + 1
