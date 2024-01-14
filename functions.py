'''
A function start with a def keyword
Followed by the name of the function and then a paranthesis containing the list of arguments
Arguments can be blank also
Function can return a value also

A function is like the maths one

    y = f(x1,x2,..)
    
    y is the return value
    f is the name of function and 
    x is the argument
'''


# def message():
#     print("Hello Kanika Mam, plz leave my hair and ear")

'''
Name of the function: message
Arguments: 
return: 
To run the functin we simply call it with the arguments
'''
# print("The function is called below")
# message()


'''
To pass argument simply put them in paranthesis
    y = f(x)
'''

# def add(a,b,c):
#     print(a+b+c)

# add("I"," was ","late")

'''
We don't always have to print
We can take the output as return
'''

# def matrix(a,b,c,d):
#     return a*d-b*c

# r1 = matrix(5,7,8,9)       # print(matrix(5,7,8,9))
# r2 = matrix(1,2,3,4)       # print(matrix(1,2,3,4))
# print(r1,r2)    

'''
given x,y,z values where 
x=workers completing task in y days 
write a function which returns the number of days required by z workers
'''
# def RequiredDays(x,y,z):
#     return y*x/z
# print(RequiredDays(2,4,4) )

'''
given x,y,z coordinates of a point
return the distance from origin respectively
'''
# def pointcoordinates(x,y,z):
#     return (x**2 + y**2 +z**2)**0.5
# print(pointcoordinates(5,6,7))

'''
string named 101010.....-binary system consider it as string not a number,find the number of 1's in the given binary number considering it as a string respectively.
'''
# def binarysystem(abcdefgh):
#     variable=0 
#     for i in abcdefgh:
#         if i=='1':
#            variable+=1
#     return variable
# print(binarysystem('1000111'))

'''
write a function in order to get the factors of the given number respectively
'''

# def factors(nums):
#     fact=[]
#     for i in range(1,nums+1):
#         if nums%i==0:
#             fact.append(i)
#     return fact
# print(factors(54))

'''
given two numbers, find the HCF of them resp
'''   
# def hcf(a,b):
#     hcfff=1
#     for i in range(1,min(a,b)+1):
#         if a%i==0 and b%i==0:
#             # if hcfff<i:  #OPTIMIZATION
#                 hcfff=i
#     return hcfff
# print(hcf(8968879867945,75898989))

'''
given two numbers, find the LCM of them resp
'''
# def LCM(a,b):
#     for i in range(1,b+1):
#         if a*i%b==0:
#             return a*i
# print(LCM(18,16))
'''
find the factorial of N 
Recuraion-nth value of a function depends upon itself or any parameter given a base case,heavy to compute
ex--f(n)=f(n-1)+f(n-2) (fibonacci series)
every function has its own base case
'''
# def factorial(N): #RECURSION
#     if N==0:  #base case
#         return 1
#     else:
#         return N*factorial(N-1)
# print(factorial(3))        

'''
fibonacci series
import-consists of some code which can we used by extracting the coded file from external
# '''

# import time

# def fibonacciseries(N):
#     if N==0:
#         return 1
#     if N==1:
#         return 1
#     else:
#         return fibonacciseries(N-1) + fibonacciseries(N-2)
    
   
# s=time.time()
# print(fibonacciseries(40))    
# f=time.time()
# print(f-s)

'''
Dynamic Programming     
Memoisation(register)-dictionary{}
'''
# import time

# def fibonacciseries(N,memo={}):
#     if N==0:
#         return 1
#     if N==1:
#         return 1
#     if N in memo.keys():
#         return memo[N]
    
#     else:
#         var = fibonacciseries(N-1,memo) + fibonacciseries(N-2,memo)
#         memo[N]=var
#         return var
    
   
# s=time.time()
# print(fibonacciseries(900))    
# f=time.time()
# print(f-s)

'''
tower of hanoi
'''
# def move(source,destination,helper,num):
#     if num==1:
#         print("move",num,"from",source,"to",destination)
#         return
#     move(source, helper,destination,num-1)
#     print("move",num,"from",source,"to",destination)
#     move(helper, destination, source,num-1)


# move("A","B", "C",3)


'''
Minimum path in the given rectangle
'''

#prerequisit: Multi-dimensional Arrays

map = [
    [0, 6, 9, 4],
    [0, 8, 2, 0],
    [4, 0, 2, 0]
]

def minimumPath(mat, path='',weight=0):
    if len(mat)==0:
        return path,weight
    if len(mat)==1 and len(mat[0])==1:
        return path,weight
    
    
        