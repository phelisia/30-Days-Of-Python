from itertools import count


fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']


fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False



# syntax
lst = list()
lst.append(list)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)


# syntax
lst = ['item1', 'item2']
# lst.insert([0], "you")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)


lst = ['item1', 'item2']
lst.pop()       # last item
# lst.pop([1])
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']


# lst = ['item1', 'item2']
# del lst[1] # only a single item
# del lst        # to delete the list completely
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[1]
# print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
# del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
# print(fruits)       # ['orange', 'lime']
# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined



lst = ['item1', 'item2']
lst_copy = lst.copy()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

#joining using plus operator

list3 = [1] + [2]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

#joining using .extend()

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', '

#reversing a list
lst = ['item1', 'item2']
lst.reverse()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]


#Declare an empty list
my_list=[]

#Declare a list with more than 5 items
my_list=['banana','berry','mango','kiwi','potato']

#Find the length of your list
my_lists=['banana','berry','mango','kiwi','potato']
print(len(my_lists))

#Get the first item, the middle item and the last item of the list
my_listss=['banana','berry','mango','kiwi','potato']
print(my_listss[1],my_listss[3],my_listss[4])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types=["Siara",23,12.5,"married","ndwaru"]
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial 
# values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
print(len(companies))

#Print the first, middle and last company
print(companies[1],companies[5],companies[6])
#Print the list after modifying one of the companies
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
companies.insert(7,"cloud")
print(companies)
#Add an IT company to it_companies
# companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
# print(companies.add(5,"Azure"))
#Insert an IT company in the middle of the companies list
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
companies.insert(8,"azure")
print(companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
for i in companies:
    print(i.upper())
    
 #Join the it_companies with a string '#;  '
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
n=['i','love','money']    
companies.extend(n)
print(companies)
print(companies + n)
#Check if a certain company exists in the it_companies list.
z='Aqutum' in companies
print(z)
#Sort the list using sort() method
companies.sort()
print(companies)
#Reverse the list in descending order using reverse() method
companies.reverse()
print(companies)
#Slice out the first 3 companies from the list
print(companies)
k=companies[ 4:-1]
print(k)
#Slice out the last 3 companies from the list
f=companies[1:-4]
print(f)
#Slice out the middle IT company or companies from the list
l=companies[3:6]
print(l)
# #Remove the first IT company from the list
# companies.pop(1)
# print(companies)

# #Remove the middle IT company or companies from the list
# companies.pop(5)
# print(companies)

# #Remove the last IT company from the list
# companies.pop(-1)
# print(companies)
# #Remove all IT companies from the list
# companies.clear()
# print(companies)

# #Destroy the IT companies list
companies=['Fb','Google','Microsoft','Apple','IBM','Oracle', 'Amazon']
print(companies)
companies.pop[3:-3]
print(companies)
new_list = []
new_list.append(companies)
print(new_list)




