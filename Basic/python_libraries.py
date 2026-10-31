# 1.python liraries— Data Structures




# a=[2,3,4,5,5,6,6,6,2,2,9,2,2,2,3,7,9]
# x=10
# #appending
# a.append(x)
# print(a)

# b=[2,3,4,5]
# extending
# a.extend(b)
# print(a)

# insert
# a.insert(0,356)
# print(a)

# remove  It raises a ValueError if there is no such item.
# a.remove(2)
# print(a)

# pop
# a.pop() #remove the last element
# print(a) # which removes the last element
# a.pop(2) # which deletes  the index number 
# print(a)

#Clear
# a.clear()
#or
# del a[:5]
# del a[5:]

#index method we can practice this 3 ways
# numbers=[10,20,30,40,50,60,70,20,80,90]
# print(numbers.index(40))

#Start at the range
# print(numbers.index(20,4)) #if not found number it raises an value error

#give an range(start and end)
# print(numbers.index(20,5,12)) 




#count
# num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# print(num.count(2))



#sort
# num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# num.sort(reverse=False) # asecnding order
# num.sort(reverse=True ) #descending order
# print(num)


#reverse
# num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# num.reverse()
# print(num)



#copy
num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]

# a=num.copy()
# print(a)
#another method
# a=num[1:] #start at index 1 to copy 
# a=num[0:3] #start at index at 0 and end 2 3 is excluded
#a=num[:3]
# print(a)



#list as a stacks
# a=[2,2,4,4,5,6,7,8,8]
# a.append(2)  #to add element
# print(a)
# a.pop()  #to remove the element from top 
# print(a)



#list as a queues
from collections import deque
a=deque(['hari','krishna','hareee'])
a.append("radhe")
print(a)
a.popleft()
a.popleft()
print(a)



































