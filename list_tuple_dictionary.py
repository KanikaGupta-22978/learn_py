'''
Lists conatin data under a single structure
for example 
    nums = [1,5,6,8,9,10]
same as strings each element is assigned an index starting from 0
Each element can be accessed by this index
'''
# nums = [1,5,6,8,9,10]
# print(nums[2])

'''
You access a range of elements just as in the strings
'''
# nums = [1,5,6,8,9,10]
# print(nums[1:5])

'''
List elements can be multiple types
    nums = [1,'Ashu',1.25]
'''
# nums = [1,'Ashu',1.25]
# print(nums[1])

'''
You can ennumerate over the elemnts with a for loop
'''
# nums = [1,5,6,8,9,5,2,87,5]
# for i in nums:
#     print(i)

'''
lists are mutable
'''
nums = [1,5,6,8,9,5,2,87,5]
print(nums)
nums[2]=7
print(nums)

nums.append(35)
print(nums)

'''
tuples are like immutable list
'''
# name=("cat","dog","rat")
# print(name[1])
# name=("cat","dog","rat")
# for i in name:
#     print(i)
# name=("cat","dog","rat")
# name[0]='peigon'
# print(name)
 
'''
dictionaries don't have index
they have a key for each value
'''
# dic = {"first":"cat","hello":10,12:"Kanika"}
# print(dic[12])
# print(dic.keys())
# print(dic.values())