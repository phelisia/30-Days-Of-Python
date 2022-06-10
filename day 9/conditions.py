#Short Hand



from locale import ABDAY_3


a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
#Nested Conditions
# a = 0
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')
# #If Condition and Logical Operators
# age=18
# user_input=int(input("Enter age: "))
# if user_input>age:
#     print('you are old enough to drive')
# else:
#     print(f'you need {age-user_input} years to learn to drive')

# my_age=25
# users_age=int(input("Enter your age: "))  
# if users_age>=my_age:
#     print(f'you are\t{users_age-my_age} older than me')
# else:
#     print('i am older than you')  
random_a=4
random_b= 3
random_a=int(input("Enter number: "))
if random_a>random_b:
    print('a is greater than b')
elif random_a<random_b:
    print('smaller than b')
else:
    print('a is equal to b')

month_now=["September", "October" ," November","December","January","February","March","April","May","June","July","August"]
month_now= str(input('enter month: ').title())
if month_now== "September":
    print('Autmn')
elif month_now== ["December","January","February"]:
    print('winter')
elif month_now== ["March","April","May"]:
    print('Spring')
else:
    print('its summer')

# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

y=100
y=int(input('Enter points: ')) 
if y==80 and y<=100:
    print("A")

elif y==70 and y<=89:
    print('B')
elif y==60 and y<=69:
    print('B')    
elif y==50 and y<=59:
    print('B')  
else:
    print('f')

fruits = ['banana', 'orange', 'mango', 'lemon']
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person=='skills':
    print(person['skills'][2])
else:
    print('this is a dictionary')    
