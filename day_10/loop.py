# count=0
# while count<5:
#     print(count)
#     count+=1
# else:
#     print(count)
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break  
# count=0
# while count<5:
#     if count==3:
#         print(count)
#         count+=1  
# language='python'
# for letter in language:
#     print(letter)
language = 'Python'
for i in range(len(language)):
    print(language[i])
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person.items():
    print(key)    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')    

# lst = list(range(11)) 
# print(lst)
# st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
# print(st) 
# lst = list(range(0,11,2))
# print(lst) # [0, 2, 4, 6, 8, 10]
# st = set(range(0,11,2))
# print(st) #  {0, 2, 4, 6, 8, 10}
num=range(10,0)
for i in num:
    print(i)
# even=range(0,100)
# zote=0
# for eve in even:
#     if eve%2==0:
#         zote+=eve
#         print(zote)

sum=range(0,100)
total=0
for all in sum:
 if all%2!=0:
   total+=all
   print(total)     
list=['banana', 'orange', 'mango', 'lemon']
for lii in reversed(list):
    
    print(lii)
    