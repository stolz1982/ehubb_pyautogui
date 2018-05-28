import keyfunction as func
import random
import time
products = [["Product 1", 590, 339], ["Product 2", 725, 336], ["Product 3", 866, 341]]
buttons = [["payment", 179, 654], ["cash", 233, 342], ["validate", 957, 181], ["next", 957, 181]]
amount = ["tendered", random.randint(10000, 20000)]

#start with intial questions
r = 0
s = 0

print('How many times the script should run?')
r = int(input())
print('How long should take the breaks between the sales?')
b = int(input())


while s < r:
    # break between the orders
    time.sleep(b)
    print "-------Start---------------"
    i = 0
    #sending product(-s) and quantities
    while i < random.randint(1, len(products)):
        n = random.randint(0, len(products) - 1)
        print products[n][0] #Product name
        print products[n][1] # x
        print products[n][2] # y
        #sending the product
#        func.keystroke_mouse(2, products[n][1], products[n][2], 1)
        #sending the quantities
 #       func.keystroke_keys(1, str(random.randint(1, 10)), 1, 0.2)
        i = i + 1

    #Pressing payment
#    func.keystroke_mouse(1, buttons[0][1], buttons[0][2], 1)

    #Pressing cash
#    func.keystroke_mouse(1, buttons[1][1], buttons[1][2], 1)

    #entering the amount of tendered
#    func.keystroke_keys(1, amount[0][1], 1, 0.2)

    #Pressing validate
#    func.keystroke_mouse(1, buttons[2][1], buttons[2][2], 1)

    #Pressing next
 #   func.keystroke_mouse(1, buttons[3][1], buttons[3][2], 1)

    print "------------Ende--------------"
    s = s + 1
