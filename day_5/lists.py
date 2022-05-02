from itertools import count


lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
girls = ["Annita","Ann","Christine","Bendette","Phelisia","Brenda","Saido","Elizabeth"]
first_item,second_item, * rest = girls
print(first_item)
print(second_item)
print(third_item)
print(rest) 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))          
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

#questions
empty_list = []
print(empty_list)
list_1 = [1,2,4,5,"Annita","Morurine",True]
print(list_1)
print(len(list_1))
print(list_1[0])
print(list_1[3])
print(list_1[6])
mixed_data_types = ["Lucy",22,12.5,"Single","11100"]
print(mixed_data_types)
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(count(it_companies))

