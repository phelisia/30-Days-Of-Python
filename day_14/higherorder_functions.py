from functools import reduce


def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(x, lst):  # function as a parameter
    sum = x(lst)
    return sum
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
a=(1,2,7)
y=sum(a)
print(y)  

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')

#python closures
# Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  
print(closure_result(10))  
#maps
#The map() function is a built-in function that takes a function and iterable as parameters.
numbers = [1, 2, 3, 4, 5] 
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))   
names=["Phelisia Jeruto","Sarah Kahaki","Lynette Jepchumba"]
def names_upper(name):
    return name.upper()
upper_names=map(names_upper,names) 
print(list(upper_names))
#Python - Filter Function
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
hard_worker=["judy","phelisia","Joana","kima","och"] 
def tia_bidii(student):
    if len(student)<4:
        return False
    else:
        return True
hard_workers=filter(tia_bidii,hard_worker)
print( list(hard_workers))   
#Python - Reduce Function
# The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable.   However, it does not return another iterable, instead it returns a single value
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total =reduce(add_two_nums, numbers_str)
print(total)   
for x in numbers:
    tot=0
    tot+=x
    print(x)   
#Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def upper(country):
    return country.upper()
new_upper=map(upper,countries)
print(list(new_upper))   

#Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def squares(squire):
    all_square=squire**2
    return all_square
newSquare_list=map(squares,numbers)
print(list(newSquare_list))    
#Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def upper_names(jina_mpya):
    changes_names=jina_mpya.upper()
    return changes_names
changedUppercase_names=map(upper_names,names)
print(list(changedUppercase_names))
#Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def containing_land(countrry):
         if "land" in countrry:
            return countrry
filtered_list=filter(containing_land,countries)
print(list(filtered_list))            
        

    


