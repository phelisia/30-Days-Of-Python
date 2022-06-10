fruits=('banana','orange','mango','lemon')
last_index=len(fruits)
print(last_index)
all_items=fruits[0:]
orange_mango=fruits[1:3]
orange_rest=fruits[1:]
negative_index=fruits[-4:-1]
print(negative_index)
print(orange_rest)
print(orange_mango)
print(all_items)
fruit_list=list(fruits)
print(fruits)
empty_tuple=()
print(empty_tuple)
sister=('chumba','sarah')
print(sister)
brother=('john','sang')
print(brother)
siblings=brother+sister
print(len(siblings))
members=('john','sarah')
family_members=members+siblings
print(family_members)
x,y,z,w,b,c=(family_members)
print(x,y,z,w,b,c)
matunda=()
vegetables=()
animal_products=()
food_stuff_tp=matunda+vegetables+animal_products
print(food_stuff_tp)
food_stuff_lt =list(food_stuff_tp)
del food_stuff_tp
print( food_stuff_lt)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Sweden' in nordic_countries)