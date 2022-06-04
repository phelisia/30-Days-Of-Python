# Arithmetic Operations in Python
# Integers

from math import floor


print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) 

# List all the arithmetic operators that can be used in Python with a brief description of each.

x= 1+1 #for addition 
print(10*10)#fro multiplication
print(5-5)#for subtraction
print(3**3)# exponation for square 
print(4//5)# Division without float or decimal point
print(5%4)#returns the remainder of the two numbers
print(5/7) #for divison

# For each of the following Python statements indicate which is an operand and which an operator.



w = 1 + 4 # + operator
x = 8 ** 5 # ** operator
y = 6 // 6 # // operator
z = 2 % 5  # % operator
#w,x,y,z are operands

# For the program below write down the expected output to the Visual Display Unit
w = 2
x = 5
y = 7

a = w + y  #9
b = y - w  #5
c = y % x  #2
d = y // w #3
e = y ** w #49
f = w * x #10
g = y / x #1.4
print(a,b,c,d,e,f,g)

# Write a program that asks the user to enter two integers. Have the program output the two integers and the result when the first number entered is raised to the power of the second number entered.
x=int(input("enter int:"))
y=int(input("enter second int:"))
if x==0:
    print(x**2)
print(x**y)    

# Write a program that asks the user to enter two integers.
# Have the program output how many times the second number can be divided into the first number.
# For example if the first number entered was 23 and the second number entered was 4 the program should report 5 times (i.e. the fractional bit is ignored). 
# You are required to implement this program using the floor operator.
a=int(input("Enter Number"))
b= int(input("Enter second number"))
if a % b == 0:
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", b)
    print(floor(a))
    
    
    
    # A 1 is always the remainder whenever an odd integer is divided by 2.
    # Write a computer program that asks the user to enter an integer (odd or even) and have it report whether the integer entered is odd. 
    # You are required to implement this program using the modulus operator and an if ... Selection construct.
  
