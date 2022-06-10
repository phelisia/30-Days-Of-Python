from multiprocessing.sharedctypes import Value


person={'lucy':'AnitaB','Age':20,'stack':['polygot','JS','Go lang','java']}
print(len(person))
print(person['lucy'])#acessing dictionary by its key
print(person['stack'])
#to check if a key exist or we can use the get method
print(person.get('is_married'))
#Adding Items to a Dictionary
person['is_married']='true'
print(person)
#Modifying Items in a Dictionary
person['is_married']='exploring'
print(person)
print('is_married'in person)
person.pop('Age')
print(person)
person.popitem()
print(person)
del person['stack']
print(person)
# Changing Dictionary to a List of Items,items() 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
dct_copy=dct.copy()#copy()
print(dct_copy)
keys=dct.keys()
print(keys)
values=dct_copy.values()
print(values)
dog={}
print(dog)
dog.update({'name':'urieboy','color':'brown & white','legs':4,'age':5})
print(dog)
student={'first_name':'','last_name':'','gender':'','age':'','marital status':'','skills':['dancing','python','cooking','sleeping']}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills']='swimming'
print(student)
student['skills']='spreading the gospel'
print(student)
print(student.items())
print(student.keys())
print(student.values())
print(student. popitem())
