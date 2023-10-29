#Program made by Johnson P. and Srinithish S.M.
#Definition of the functions for all the operations

#import of math module for trignometric ratio calculation
import math

def add():
    num1=float(input("\nEnter Number 1: "))
    num2=float(input("Enter Number 2: "))
    print("Addition of",num1,"and",num2,"is",num1+num2)
    
def subtract():
    num1=float(input("\nEnter the number you want to subtract from: "))
    num2=float(input("Enter the number you want to subtract: "))
    print("Subtraction of",num2,"from",num1,"is",num1-num2)
    
def multiply():
    num1=float(input("\nEnter Number 1: "))
    num2=float(input("Enter Number 2: "))
    print("Product of",num1,"and",num2,"is",num1*num2)

def divide():
    num1=float(input("\nEnter Number 1: "))
    num2=float(input("Enter Number 2: "))
    print("Division of",num1,"and",num2,"is",num1/num2)

def power():
    num1=float(input("\nEnter number to get power of: "))
    num2=float(input("Enter the power: "))
    print("Power of",num1,"to",num2,"is",pow(num1,num2))
    
def root():
    num1=float(input("\nEnter the number to get root of: "))
    num2=float(input("Enter the power of 1/x: "))
    print(num2,"Root of",num1,"is",pow(num1,1/num2))
    
def trig():
    flag_ = 0
    while True:
        try:
            print("\n1.Sin\n2.Cos\n3.Tan")
            flag_=int(input("Enter the number to enter the operation: "))
            if flag_ not in [1,2,3]:
                raise Exception
            break
        
        except:
            print("Invalid Input")
            continue
        
    while True:
        try:
            if flag_==1:
                deg = float(input("\nEnter the degrees: "))
                print("Sin of the given input is",math.sin(math.radians(deg)))
                break
                
            elif flag_==2:
                deg = float(input("\nEnter the degrees: "))
                print("Cos of the given input is",math.cos(math.radians(deg)))
                break
            
            elif flag_==3:
                deg = float(input("\nEnter the degrees: "))
                print("Tan of the given input is",math.tan(math.radians(deg)))
                break
        except:
            print("Invalid Input")
            continue
    
def log():
    flag_=0
    while True:
        try:
            print("\n1.Logarithm\n2.Antilogarithm")
            flag_=int(input("Enter a number to enter the operation: "))
            if flag_ not in [1,2]:
                raise Exception
            break
        except:
            print("Invalid Input")
            continue
    
    while True:
        base_=0
        try:
            if flag_==1:
                base = input("\nEnter the base (e - Natural Logarithm): ")
                if base == 'e':
                    base = math.e
                    base_='e'
                else:
                    base = float(base)
                    base_=base
                num = float(input("Enter the number to get log of: "))
                print("Logarithm base",base_,"of",num,"is:",math.log(num,base))
                break
                    
            elif flag_==2:
                base = input("\nEnter the base (e - Natural Antilogarithm): ")
                if base == 'e':
                    base = math.e
                    base_='e'
                else:
                    base = float(base)
                    base_=base
                num = float(input("Enter the number to get antilog of: "))
                print("Antilogarithm base",base_,"of",num,"is:",pow(base,num))
                break
            
        except:
            print("Invalid Input")
            continue
                                    
#Making decision variables global to avoid errors
global continue_var_dec,continue_var,m,n,flag

continue_var_dec=True #For starting the program
operation_list=range(1,9) #For checking if the input operation is within range

#Menu driven function calling
while continue_var_dec:
    try:
        print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Root\n7.Trignometric Ratios\n8.Logarithmic Functions")
        flag=int(input("Enter the number to enter the operation: "))
        if flag not in operation_list:
            raise Exception
    except:
        print("Invalid Input\n")
        continue

    while True:
        if flag==1:
            while True:
                try:
                    add()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==2:
            while True:
                try:
                    subtract()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==3:
            while True:
                try:
                    multiply()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==4:
            while True:
                try:
                    divide()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==5:
            while True:
                try:
                    power()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==6:
            while True:
                try:
                    root()
                    break;
                except:
                    print("Invalid Input")
                    continue
            break
        
        elif flag==7:
            trig()
            break
        
        elif flag==8:
            log()
            break
            
    while True:    
        try:
            continue_var=(input("\nDo you want to continue the program?(y/n): "))
            if continue_var not in ['y','n']:
                raise Exception
            break
        except:
            print("Invalid Input")
            continue
            
    if continue_var=='y':
        continue_var_dec=True
    elif continue_var=='n':
        continue_var_dec=False

#End of the program
