# def num(n):
#     counter = 1
#     for i in range(1,n+1):
#         counter*=i
#     return counter
# print(num(6))    
from matplotlib.cbook import flatten


def nums(a):
    b=1
    for i in range(1,b+1):
        b*=i
    return(b)
print(nums(6))

b=[[1,2,3,4],[5,6,7,8]]
for i in b:
    for items in b:
        print(flatten(items))