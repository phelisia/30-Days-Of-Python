# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

#By using first, second and last characters of the string, create a new string.
name= "Sharon"
print(name[0],name[1],name[-1])

#Replace the (.) with (!)
names="Sharon."
print(names.replace(".","!"))

#Now make everything uppercase.
namer="sharon"
print(namer.upper())

#Make the string so that everything is properly and first letter is capital with one function.
nawe="sharon"
print(nawe.title())

#Does the string start with an A?
nase="sharon"
print(nase.startswith("A"))
print(nase.endswith("n"))

#Using .index() method, identify the index of character: (v).
nate="sharon"
print(nate.index("n"))

#Using .find() method, identify the index of character: (m).
nake="sharon"
print(nake.find("a"))

#Try to see what results you get looking for character: (X). First with .
#find() method and then with .index() method.
def fin():
    namew="sharon"
    print(namew.find("X"), namew[5])
fin()    

#Which character occur more often in the string? "a" or "o" ? 
# Print both counts inside the print function.
namet="sharon"
print(namet.count("a"),namet.count("o"))

#Print the types of two given variables with the print function.




#What is the length of the given string?
same="sharon"
print(len(same))

 #Create a string made of the first, middle and last character
a="Lubembe"
print(a[0],a[3],a[-1]) 

#Create a string made of the middle three characters
def combine(b,c):
    b="lubembe"
    c="anota"
    print(b[4],b[5]+c[4],c[5])
    
#reversing
v="lubembe"
print(v[::-1])
      
    



# #Append new string in the middle of a given string
def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)



a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#It is possible to skip characters while slicing by passing step argument to slice method.
m="lubembe"
pto = m[0:6:2] #
print(pto) # Pto

#expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
