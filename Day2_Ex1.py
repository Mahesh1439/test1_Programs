print("Welcome to swapping of two numbers")
num1=input("Enter 1st number")
num2=input("Enter 2nd number")
if(num1.isdigit() & num2.isdigit()):
    print("Before swapping")
    print(f"num1 is {num1} and num2 is {num2}")
    swapNum=num1
    num1=num2
    num2=swapNum
    print("After Swapping")
    print(f"num1 is {num1} and num2 is {num2}")
else:
    print("Invalid input")