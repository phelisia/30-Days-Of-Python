
fruits = {'banana', 'orange', 'mango', 'lemon'}
#We use len() method to find the length of a set.
print(len(fruits))
#To check if an item exist in a list we use in membership operator.
print('banana' in fruits)
#Once a set is created we cannot change any items and we can also add additional items.
#Add one item using add()
fruits.add("kiwi")
print(fruits)
#Add multiple items using update() The update() 
# allows to add multiple items to a set. The update() takes a list argument.
fruits.update(['lime','avocado'])
print(fruits)
#Removing Items from a Set
fruits.remove('lime')
print(fruits)
#The pop() methods remove a random item from a set and it returns the removed item.

y=fruits.pop()
print(y)
#clear deletes the items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

#del deletes a set

#Converting List to Set
a=[1,2,2,3,4,5,6,7,8,]
print(set(a))
#Joining Sets
b={2,3,4,5,7,8,4,45,}
c={1,2,3,4,5,6,76,7,87}
print(b .union (c))

#Update This method inserts a set into a given set
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) 

#Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

#Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers))

#Checking the Difference Between Two Sets

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

#Finding Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

#Joining Sets
e={1,2,3,4,5}
f={6,7,8,9}
print(e.isdisjoint(f))

#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Nissan")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update('n','m','w')
print(it_companies)

#Remove one of the companies from the set it_companies
y=it_companies.pop()
print(y)



