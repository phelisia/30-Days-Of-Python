#Multiline string is created by using triple single (''') or triple double quotes (""")
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

#We can connect strings together. Merging or connecting strings is called concatenation.
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
v='My house is in nairobi'
print("I am going to ",v,)

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f)

x, y, z = (i*i+i for i in range(6) if i%2==0)
print(x, y, z)
x="hello \"world\""
print(x)
print("""what 
      about""")
y="hello am 10 years old"
print(y[2::])
print(len(x))
print(y.strip("h"))
#returns occurrences of substring in string, count(substring, start=.., end=..). 
# The start is a starting indexing for counting and end is the last index to count.

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2` 

# f="tomorrow"
# r=[]
# for ch in r:
#     if ch not in r:
#         ch+=r
#         print(r)
        
f="tomorrow"
t=""
for ch in f:
    if ch not in t:
        t=t+ch
        print(ch)  
        

   
# num=int(input("Enter number:"))
# num=0
# while
#    rev=str(num)
#    num_reverse=rev[::-1]  
#    if rev==num_reverse:
#     print(num,'IS PALINDROME') 
#     break
# int(rev)+int(num_reverse)


# def palindrome(s):
#     return s==s[::-1]
# print(palindrome('abba'))
# print(palindrome('zippy'))

def pali(words):
    for word in words:
        if word==word[::-1]:
            print(True)
        else:
            print(False)
pali(input("Enter words:"))                
  

        
  