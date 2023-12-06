def quitA():
    quitA = str(input('do you want to go futher (yes) or (no)')) # this
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

def calculator(): 
    global num1,num2,operation,calculator 
    print('Welcome to my calculator')
    quitA()

    num1 = float(input('Enter your first number \n'))
    quitA()
    num2 = float(input('Enter your second number \n'))
    quitA()
    operation = input('Please enter one of the following ( +, -, /, *, **, %)\n') 
    quitA()


    if operation == '+':
        print(num1 + num2)
        quitA()
        calculator()
    elif operation == '-':
        print(num1 - num2)
        quitA()
        calculator() 
    elif operation == '/':
        print(num1 / num2) 
        quitA()
        calculator()  
    elif operation == '**':
        print(num1 ** num2)
        quitA() 
        calculator()  
    elif operation == '%':
        print(num1 % num2) 
        quitA()
        calculator()  
    else:
        print(num1 * num2)
        quitA()
        calculator()

calculator() 