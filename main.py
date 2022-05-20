#When importing a module you use the import keyword  and the file you are importing from
# from day_12.myModule import generate_name
# import mymodule
# print(generate_name('phelisia','jeruto'))   
#Changing a module name
from day_12.myModule import generate_name as fullname
print(fullname('phelisia','jeruto'))
#Different module
#python module we have inbuilt function like os module,sys module,math module statistic module string module random module
#OS Module
#Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.
import os
os.getcwd()
#sys Module
#The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
# import sys
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
#statistic module
 # importing all the statistics modules
#he statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
#math module
#Module containing many mathematical operations and constants.
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
#checking what the module contian
# help(math)
#importing everything in the math module
from math import *
print(pi)

#stringModule
import string
print(string.ascii_letters)
print(string.digits)
#Random Module
from random import random, randint
# print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
# print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
from day_12.myModule import random_user_id
print(random_user_id(string.digits))
