#single line comment
"""
this is a multiline comment
"""
#list[]  mutable
from unittest import result


list=['phelisia','kibet']
print(list)
#dictionary{} unpordered collection in a key value pair format
name={'firstname':'jeruto',
'lastname':'sang',
'country':'finland',
'is_married':'true',
'skills':['JS','React','Node','Python']
}
print(name)
#tuple () orderd and are immutable
tuple=('karime','pascalne','ampuriira')
print(tuple)
# set {} are unorderd  you can add or remove elements
set={2,4,5,'possibilities'}
print(set)

#VCheck the data types of the following data:
#10
#9.8
#3.14
#4-4j
#['asabeneh','python','finland']
# your name
#your family name
#your country

w=10
print(type(w))
x=9.8
print(type(x))

y=3.14
print(type(y))

z=4-4j
print(type(z))
yourname='phelisia'
print(yourname)
yourfamilyname='sangs'
print(yourfamilyname)
yourcountry='kenya'
print(yourcountry)
#Find an Euclidian distance between (2, 3) and (10, 8)
#this is the formular
#squarerootof(x2-x1)**2+(y2-y1)**2
x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
distance=((((x2 - x1 )**2) + ((y2-y1)**2) )**2)
print("distance between",(x1,x2),"and",(y1,y2),"is:",distance)
