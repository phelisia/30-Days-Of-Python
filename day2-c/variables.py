#variables
first_name = "Siara"
last_name = "Lubembe"
country = "Kenya"
status = "married"
city = "Nairobi"
age = 20
skills =["python","JavaScript","Kotlin"]
personal_info={
    "first_name":"Siara","last_name":"Lubembe","country":"kenya"
}
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', status)
print('Skills: ', skills)
print('Person information: ', personal_info)

#multiple function
first_name = "Siara"
last_name = "Lubembe"
country = "Kenya"
status = "married"
city = "Nairobi"
age = 20
skills =["python","JavaScript","Kotlin"]
personal_info={
    "first_name":"Siara","last_name":"Lubembe","country":"kenya"
}
# first_name, last_name, country, age, status = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, status)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', status)

#input function
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#checking datatypes
first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))  


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(str(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_int = '10.9'
num_float = float(num_int)
print('num_float:', num_float)   # 10.0
print (int(num_float))


# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)  







a = "Virgin" 
b = "Mojito" 
print (f"Hello my name is {a},and my second name is {b}")
v = "Moscow" 
c = "Mule" 
print (f"Hello my name is {c},and my second name is {v}")

     
a = "Virginy" 
b = "Mojitoo"    
print("Hello my name is " + a , "and my second name is " +b)  

s='florida dolphins'
print(s.title())


d = "Hello world"
print(reversed(d))


r = "Hello world"
print(r.upper())
print(r.lower())