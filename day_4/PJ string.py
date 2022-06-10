from ntpath import join


print('God has ordained me blessed me set me apart and thats why "am a winner"')
# Language="Python"
# a,b,c,d,e,f=Language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
Language="python"
first_three=Language[0:3]
print(first_three)
last_three=Language[3:]
print(last_three)
# reversing string
greeting='Hello words'
print(greeting[::-3])
# skipping characters in a string

Language="Python"
pto=Language[0:6:2]
print(pto)
challenge="thirty days of python"
# checking last character of astring
print(challenge.rfind('i')) 
challenge='30'
# checks if anumber is a digit
print(challenge.isdigit())   
check_variable='bythonDjango'
# checks if anumber  is a valid variable name
print(check_variable.isidentifier())
web_tech=['html','css','javascript','python']
# used to join strings
shikanisha=''.join(web_tech)
print(shikanisha)
# strip removes characters in a string
toa_zote="Maryann"
print(toa_zote.strip("ann"))
list="thirty,days,of,python"
print(list.swapcase())
conatete='Thirty', 'Days', 'Of'
join_all=''.join(conatete)
print(join_all)
Concatenate= 'Coding', 'For' , 'All'
one_string=''.join(Concatenate)
print(one_string)
comapany="codinG for All"
print(len(comapany))
print(comapany.upper())
print(comapany.lower())
print(comapany.swapcase())
print(comapany.title())
print(comapany.capitalize())
print(comapany.strip('codinG'))
print(comapany.replace('codinG','python'))
spl_it="CodingForAll"
print(spl_it.split(' '))
print(spl_it[0])
print(spl_it.rindex('All'))

tech_companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(tech_companies.split(','))
# "Create an acronym or an abbreviation for the name 'Python Fo
s = "Coding For All"
s1 = s.split()
l = []
for i in s1:
    if(i != "and"):
        a = i[0]
        l.append(a)
b = "".join(l)
print(b.upper())    
# def fxn(stng):
    
#     # get all words
#     lst = stng.split()
#     oupt = ""
      
#     # iterate over words
#     for word in lst:
        
#         # get first letter of each word
#         oupt += word[0]
          
#     # uppercase oupt
#     oupt = oupt.upper()
#     return oupt
  
  
# # input string
# inpt1 = "Coding For All"
  
# # output acronym
# print(fxn(inpt1))

short_name="Python for all"
word=short_name.split()
empty_words=[]
for letters in word:
    if (letters!="and"):
        words=letters[0]
        empty_words.append(words)
        join_all="".join(empty_words)
        print(join_all.upper())



# Use index to determine the position of the first occurrence of C in Coding For All.
first_occurence="Coding Cor all"
print(first_occurence.rfind('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(first_occurence.find('o'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
find_firstindex='You cannot end a sentence with because because because is a conjunction'
print(find_firstindex.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_out="You cannot end a sentence with because because because is a conjunction"
print(slice_out.strip("because"))
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
starrt="coding for all"
print(starrt.endswith("all"))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
remove_spaces='   Coding For All      ' 
print(remove_spaces.strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
check_varaible="30DaysOfPython"
check="thirty_days_of_python"
print(check_variable.isidentifier())
print(check.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joinall='#\t'.join(libraries)
print(joinall)
sentence="I am enjoying this challenge.\nI just wonder what is next."
print(sentence)
print(sentence.expandtabs(10))
Name,Age,Country,City=["lucy\t",23,"\tKenya\t",'Nairiobi\t']
print(Name,Age,Country,City)
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with {radius} is 314 meters square.")
