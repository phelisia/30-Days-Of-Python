def function_name():
    
# Calling a function
 function_name()
# def generate_Name():
#     first_name='Phelisia'
#     second_name='Jeruto'
#     Career='Software Engineer'
#     Faith='Christian'
#     Employment='employed at Turing'
#     life=first_name + second_name + Career + Employment + Faith
#     print(life)
# generate_Name()
#Function Returning a Value - Part 1
def generate_full_Name():
    first_Name='Phelisia'
    Second_Name='Jeruto'
    full_name=first_Name+Second_Name
    return full_name
print(generate_full_Name())

def greeting(salamu):
    message=salamu+'Phelisia Jeruto'
    print(message)
greeting('Habari Yako')  

def all_numbers(num1,num2):
    sumup=num1+num2
    return sumup
print(all_numbers(12,4))    

def print_name(firstname):
    return firstname
print('phelisia')
def sum(a,b):
    total=a+b
    print(total)
sum(10,20)   

def area_of_circle(r):
    area=3.14*r**2
    print(area)
area_of_circle(7)  

#Arbitrary Number of Arguments
def all_add_num(*nums):
    total=0
    for num in nums:
        if num==int:
            total+=num
        else:
            'mixed type'
    return num 
print(all_add_num(12,14,16,True,'phelisia'))   

# def convert_celsius(c):
#     temprature=(c x 9/5) + 32
#     return temprature
# convert_celsius(7)    


def check_season(month):
    summer=('January','february','march','April')
    Autumn=('may','june','july')
    Winter=('august','september','october')
    Spring =('november','December')
    mwezi=0
    for mwezi in month:
        if mwezi==summer:
            print('summer')
        elif mwezi==Autumn:
            print('autumn')
        elif mwezi==Winter:
            print('winter')
        elif mwezi==Spring:
            print('spring')
        else:
            print('month not in season ')    
check_season('January')                




    


    



