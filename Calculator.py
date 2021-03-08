import time

def add(x,y):
    return x + y
    
def sub(x,y):
    return x - y
    
def div(x,y):
    return x / y
    
def multi(x,y):
    return x * y


print("What do you want to do \n"
      "1. Add \n"
      "2. Subtract \n"
      "3. Division \n"
      "4. Multiplication \n")

select = int(input("Select what you want to do from 1,2,3,4 : "))
time.sleep(0.8)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if select==1:
    print("The answer is", add(x,y))
    
if select==2:
    print("The answer is", sub(x,y))
    
if select==3:
    print("The answer is", div(x,y))
    
if select==4:
    print("The answer is", multi(x,y))