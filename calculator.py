#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from art import logo

def add (n1 , n2) :
    return n1 + n2


def subtract (n1 , n2) :
    return n1 - n2
    
    
def multiply (n1 , n2) :
    return n1 * n2


def divide (n1 , n2) :
    return n1 / n2

def power (n1 , n2) :
    return pow(n1 , n2)


operation = {
    "+" : add ,
    "-" : subtract ,
    "*" : multiply ,
    "/" : divide ,
    "^" : power
}

def calculator() : 
    print(logo)
    num1 = float(input("What's the first number? :  "))
    
    for symbol in operation :
        print(symbol)
    
    should_continue = True
    while should_continue :
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? :  "))
        
        which_operation = operation[operation_symbol]
        answer = which_operation(num1 , num2)
        
        print(f"{num1}{operation_symbol}{num2}={answer}")

        continue_with_answer = input(f"Type 'continue' to continue calculating by {answer} or type 'new' to start a new calculation and 'exit' to exit")
        
        if continue_with_answer == 'continue' :
            num1 = answer
        elif continue_with_answer == 'new' :
            should_continue = False
            calculator()
        else :
            print("Good Bye!")
            return


calculator()

