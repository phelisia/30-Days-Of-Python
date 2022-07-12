# # syntax
# empty_tuple = ()
# # or using the tuple constructor
# empty_tuple = tuple()

# tpl = ('item1', 'item2','item3')
# tpl = ('item1', 'item2', 'item3')
# first_item = tpl[0]
# second_item = tpl[1]
# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[0]
# second_fruit = fruits[1]
# last_index =len(fruits) - 1
# last_fruit = fruits[last_index]

# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[0:4]         # all items
# all_items = tpl[0:]         # all items
# middle_two_items = tpl[1:3]  # does not include item at index 3
# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[0:4]    # all items
# all_fruits= fruits[0:]      # all items
# orange_mango = fruits[1:3]  # doesn't include item at index 3
# orange_to_the_rest = fruits[1:]

















#Create an empty dictionary called dog
#Add name, color, breed, legs, age to the dog dictionary
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

from itertools import count
from this import d


dog={"name":"Bruno","color":"Black","breed":"chiwawa","legs":4,"age":32}
student={"FirstName":"Siara","lastName":"Lubembe","gender":"female","age":43,"maritalStatus":"married","skills":["Python","Kotlin","Js","IOt"],"country":"Kenya","city":"Nairobi"}
#Get the length of the student dictionary
print(len(student.values()))

#Get the value of skills and check the data type, it should be a list

print(student["skills"])
print(type(["skills"]))

#Modify the skills values by adding one or two skills
d['skills']='Java'
print(d)
#Get the dictionary keys as a list
print(list(student))
#Get the dictionary values as a list
print(student.values())
print(student.keys())
#Change the dictionary to a list of tuples using items() method
print(student.items())
#Delete one of the items in the dictionary
print(student.pop("city"))
#Delete one of the items in the dictionary
fruits=('banana','siara','anota','lubembe','mango')
print(len(fruits))
print(fruits[2])
print(fruits[-2])
print(fruits[2::])
print(fruits[::2])
print(list(fruits))
print('apple' in fruits)
fruit=('kiwi','apple','mango')
names=('siara','anota','lubembe')
print(fruit+names)
del(names)
# print(names)
#Create an empty tuple
name=()
brother=('eric','valentine','felix','evans')
sister=('maureen','sharon')
siblings= brother+sister
print(siblings)
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
d=list(siblings)
d.append("betty")
d.append("lubembe")
print(d)
print(tuple(d))
#Unpack siblings and parents from family_members
d=(20,"siara","c")
(age,name,studies)=d
print(name)
print(age)

# def add_string():
  
#   a="Siara"
#   length = len(a)
# if length > 3:
#     if a[-3:] == 'ing':
#       a += 'ly'
#     else:
#       str1 += 'ing'
#     print(a)
#Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("mango")
vegetables=("Cabbage")
animal=("Hyena")
food_stuff= fruits + vegetables + animal
y=list(food_stuff)
print(y)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
# print(list(food_stuff))


# fruits=("mango","cabbage","hyena")
# y=list(fruits)
# print(y)

# #swapping the first and last numbers in a list
# numbers=[2,3,4,5,6]
# numbers[0],numbers[-1]=numbers[-1],numbers[0]
# print(numbers)
# #Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# del(food_stuff[1])


def listx():
  k=[12,23,34,45,56]
  for i in k:
    if i[0]==i[4]:
      print("true")
    else:
      print("false")  
listx()      


  