# set_one={'blessed','phelisia','Anointed','Favoured'}
# print(len(set_one))
# set_one.add('chosen')
# print(set_one)
# set_one.update(['prayerful','dedicated','smart','ambitious','patient'])
# print(set_one)
# set_one.pop()
# print(set_one)
# set_one.remove('patient')
# print(set_one)
# del set_one
# print(set_one)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}#Union This method returns a new set,
#  Update This method inserts a set into a given set
print(fruits.intersection(vegetables))#Intersection returns a set of items which are in both the sets.
essentials=fruits.union(vegetables)
print(essentials)
#Supper set: issupperset()->The issuperset() method returns True if a set has every elements of another set (passed as an argument)
#Sub set: issuset->The issubset() method returns True if all elements of a set are present in another set (passed as an argument)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
#.difference It returns the difference between two sets.
#Symmetric Difference,It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
#Joining Sets,We can check if two sets are joint or disjoint using isdisjoint()
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(['skyGarden','Twiga','AfricaStocking','Xentova'])
print(it_companies)
it_companies.remove('Oracle')
print(it_companies)
#The discard() method removes the specified item from the set. This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
it_companies.discard('Oracle')
print(it_companies)
A={'a','b','c','d','e','f','g','h','i','j'}
B={'a','b','c','d'}
A.update(B)
A.intersection(B)
print(A)
A.issubset(B)
print(A)





