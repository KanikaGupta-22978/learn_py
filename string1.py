"""
Printing a string
"""
# print("Kanika Gupta")


'''
Varibles containg strings

'''

# name = "Kanika Gupta"
# print(name)
# print("name")

'''
variable is name
value of the variable is "Kanika Gupta"
if I print(name)
'''


'''
Operation of strings
1. Concatenation - Adding two string
        'Kanika' + 'Ashutosh'  = 'KanikaAshutosh'
'''

# name="Kanika"
# girl="Ashutosh"
# print(name)
# print(girl)
# print(name+girl)
# print( name + " " + girl )


'''
Length of the string - number of characters
    a = 'Kanika'
    len(a) will be 6
'''

# name="Ashutosh Vishwakarma"
# names="Kanika Gupta"
# length=len(name)
# length1=len(names)
# print(length,length1)


'''
Accessing characters from string
    There is an index associated with each character
    It starts with 0
    For example lets have
    name = "Kanika"
    
    characters      Index
    ---------------------
    K               0
    a               1
    n               2
    and so on
    
    if I say
    
    
    secondLettor = name[1]
    secondLettor will contain 'a'
    
'''
# name="Ashutosh Vishwakarma"
# print(name[12])

'''
For accesing a range of characters say substring
We may say like this

    name = "Kanika"
    subname = name[2:4]
    subname will conatin 'ni'
    Because
    
    Index           Character
    --------------------------
    0               K
    1               a
    2               n
    3               i
    4               k
    5               a
    
    if I give the name range name[2:4] then 4 is excluded
    Hence we get        name[2:4] as 'ni'
    
    Question: If I say name[6]
    Answer: It will give error, Index Out of Range
'''
# name="Ashutosh Vishwakarma"
# print(name[9:20])


'''
Some tricks in accesing range
if we say
    name = 'Kanika Gupta'
    name[2:6] will be   'nika'
    name[2:] will be    'nika Gupta'
    name[:4] will be    'Kani'
'''
# name = 'Kanika Gupta'
# print(name[2:6]) 
# print(name[2:] )
# print(name[:4] )

'''
Negative Indices are allowed
It starts with -1 for the last character and moves to left
    name = 'Kanika'

    Index           Character
    --------------------------
    -6               K
    -5               a
    -4               n
    -3               i
    -2               k
    -1               a
    
'''
# name="Ashutosh Vishwakarma"
# print(name[-11:])

'''
Print all vowels in the given string
string = "My name is Ashutosh Vishwakarma. I am with Kanika Gupta"
'''
# string = "My name is Ashutosh Vishwakarma. I am with Kanika Gupta"
# for i in range(0,len(string)):
#     if  (string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u') :
#         print(string[i])

'''
There is a problem in the code.
It doesnot consider capital vowels
Solution:
    1. Add five more coditions
    2. Bring the string to lower or upper case and then match
'''


'''
Som we need to manipulate string case
    s = "Kanika Gupta"
    so s.lower() then it's 'kanika gupta'
    also s.upper() then it's 'KANIKA GUPTA'
'''
# name="Ashutosh Vishwakarma"
# print(name)
# print(name.lower())
# print(name.upper())


'''
Now use it to rewrite and not miss the capital letters
'''
# string = "My name is Ashutosh Vishwakarma. I am with Kanika Gupta"
# string=string.lower()

# for i in range(0,len(string)):
#     if  (string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u') :
#         print(string[i])




'''
Strings are immutable that is you cant change the element
'''
# s = 'kanika gupta'
# s[0] = 'K'
# print(s)

# #this throws an error

'''
you can enumerate over string with for loop
'''
# s = "Kanika Gupta"
# for i in range(0,len(s)):
#     print(s[i])

# for i in s:
#     print(i)
