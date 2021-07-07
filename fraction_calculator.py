#fraction calculator

import time

whole = int(input("enter the whole number >> "))
div = int(input("enter the divident >> "))
num = int(input("enter the numerator >> "))

deev = str(div) #div

op = input() #operation

def convert():
    print(whole*div+num)
    print("--\n"+deev)
    
def add():
    print(whole*div+num)
    print("--\n"+deev)

if op == "convert":
    i()
    convert()
elif op == "add":
    whole2 = int(input("enter the whole number for the 2nd number >> "))
    div2 = int(input("enter the divident for the 2nd number >> "))
    num2 = int(input("enter the numerator for the 2nd number >> "))
    time.sleep(1)
    add()
