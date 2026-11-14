# # 1.python liraries— Data Structures
'''
5. Data Structures
5.1. More on Lists
5.1.1. Using Lists as Stacks
5.1.2. Using Lists as Queues
5.1.3. List Comprehensions
5.1.4. Nested List Comprehensions
5.1.5. Unpacking in Lists and List Comprehensions
5.2. The del statement
5.3. Tuples and Sequences
5.4. Sets
5.5. Dictionaries
5.6. Looping Techniques
5.7. More on Conditions
5.8. Comparing Sequences and Other Types'''

'''
| Data structure | Example | Main property |
|---             |---      |---             |
| List  |       `[10, 20, 30]` | Ordered, mutable |
| Tuple |       `(10, 20, 30)` | Ordered, immutable |
| Set   |       `{10, 20, 30}` | Unique elements,unordered |
| Dictionary |  `{"a": 10}`     | Key-value pairs ,ordered|
'''
# '''List'''.........................
# # a=[2,3,4,5,5,6,6,6,2,2,9,2,2,2,3,7,9]
# # x=10
# # #appending
# # a.append(x)
# # print(a)

# # b=[2,3,4,5]
# # extending
# # a.extend(b)
# # print(a)

# # insert
# # a.insert(0,356)
# # print(a)

# # remove  It raises a ValueError if there is no such item.
# # a.remove(2)
# # print(a)

# # pop
# # a.pop() #remove the last element
# # print(a) # which removes the last element
# # a.pop(2) # which deletes  the index number 
# # print(a)

# #Clear
# # a.clear()
# #or
# # del a[:5]
# # del a[5:]

# #index method we can practice this 3 ways
# # numbers=[10,20,30,40,50,60,70,20,80,90]
# # print(numbers.index(40))

# #Start at the range
# # print(numbers.index(20,4)) #if not found number it raises an value error

# #give an range(start and end)
# # print(numbers.index(20,5,12)) 




# #count
# # num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# # print(num.count(2))



# #sort
# # num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# # num.sort(reverse=False) # asecnding order
# # num.sort(reverse=True ) #descending order
# # print(num)


# #reverse
# # num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]
# # num.reverse()
# # print(num)



# #copy
# num=[2,40,40,50,70,90,89,7899,58,2,3,2,2,2,2]

# # a=num.copy()
# # print(a)
# #another method
# # a=num[1:] #start at index 1 to copy 
# # a=num[0:3] #start at index at 0 and end 2 3 is excluded
# #a=num[:3]
# # print(a)



# #list as a stacks
# # a=[2,2,4,4,5,6,7,8,8]
# # a.append(2)  #to add element
# # print(a)
# # a.pop()  #to remove the element from top 
# # print(a)



# #list as a queues
# from collections import deque
# a=deque(['hari','krishna','hareee'])
# a.append("radhe")
# print(a)
# a.popleft()
# a.popleft()
# print(a)





#List Comprehensions
# xx=[0,1,2,3,4,5,6]
# squares=[x**2 for  x in xx if x>3]
# print(squares)

# square_num=[x**2 for x in range(5)]
# print(square_num)


# square_num_list=[x**2 for x in [1,2,3]]
# print(square_num_list)


# strings=["  hello  world!","Good Morning!  "]
# pr_strings=[strs.strip() for strs in strings]
# print(pr_strings)


# list_com=[abs(x) for x in [-4,-3,-2,2,3,4]]
# print(list_com)



#abs:abs() gives the distance from zero, without considering positive or negative direction.




#nested list Comprensions.......................
'''
matrices=[[1,2,3],[4,5,6],[7,8,9],[6,6,7],[8,9,9]]
transposed=[]
for i in  range(3):
    transposed_of_rows=[]
    for j in (matrices): #it visits every list
        transposed_of_rows.append(j[i])
    transposed.append(transposed_of_rows)   
print(transposed) 

#this is one line
nest_list_com=[[i[j] for i in (matrices)] for j in range(3)]
print(nest_list_com)

using_zip=list(zip(*matrices))
print(using_zip)
'''

'''
zip() combines elements at matching positions.
*matrix unpacks the rows as separate arguments.
list() converts the result into a list.
'''









#Unpacking in Lists and List Comprehensions.........................................................
'''
x=[1,2,3]
y=[0,*x,4]
print(y)
'''
'''
x=1
y=[0,*x,4]
print(y)
# TypeError: Value after * must be an iterable(list,numbers,strings,tuple), not int
'''
'''
x=1,2
y=[0,*x,4]
print(y) #output:[0, 1, 2, 4]
'''
'''
x="hello!","World"
y=[0,*x,"strings"]
print(y)
'''
'''
x=(1,2,3,'Hello!')
y=[0,*x,'World!']
print(y)
'''
'''
- * → Unpacks elements.
- Iterable → Something you can go through element by element, like a list, tuple or string.
- TypeError → Operation used with an unsuitable type.( i mean single like integer)
'''
'''
x={344:"yui","kkk":"hj"}
y=[0,*x,8]
print(y)  #output:[0, 344, 'kkk', 8]
'''




'''
 5.2. The del statement¶.........
| Feature |               remove() | pop() | del |
|         
|Removes by|              Value   | Index | Index / slice |
|Returnsremovedvalue?     | No   |  Yes   | No |
| Example |              `a.remove(20)` | `a.pop(1)` | `del a[1]` |
'''
# Delete one element
'''
a= [10, 20, 30, 40]
del a[0]
print(a)
'''
# Delete elements using slicing
'''
a=[2,3,4,5,6,7,77,90]
del a[2:5]
print(a)
'''


# deleting all elements
'''
a=[78,79,699,5790]
del a[:]
print(a)
'''

#delete a variable
'''
b=[7,57,890]
del b
print(b)
'''


#Tuple....................
"""
a=(1,2,3,4,"HEllo!","World",7899)
print(a)
print(a[4])
"""
# Immutable – Cannot Change
'''
t=(10,20,30)
t[0]=100
print(t)
'''
'''TypeError: 'tuple' object does not support item assignment'''

# Tuple Packing
'''Putting multiple values together into a tuple.'''
'''Python automatically understands comma-separated values as a tuple without anything'''
'''
t=10,20,30
print(t)
'''
# Sequence Unpacking
'''
a,b,c=(10,20,30)
print(a)
print(b)
print(c)
'''



# Empty Tuple and Single-Element Tuple
"""
a=()
b=(5)
print(a)  #output:()

print(b) #output:5 but not in tuple
'''to get that we should write ,'''
b=(5,)
print(b) #output:(5,)


'''
Tuple = ordered collection. Ordered collection means elements are stored in a fixed order, and each element has an index (position).
Tuple is immutable.
Tuple uses ().
Packing = putting values together.
Unpacking = assigning values to separate variables.
'''
"""




"""
# Sets in Python............................
basket = {"apple", "orange", "apple", "banana"}
print(basket)

#output: {'apple', 'banana', 'orange'}

'''
Properties of Sets
- Unordered – No fixed index or position.
- No duplicates – Stores unique values.
- Mutable – We can add or remove elements.
- Uses {}.
'''


# Empty Set
a={} #this is empty dictionary
print(a)

a=set() #empty set
print(a)



# Membership Testing (in)
a = {10, 20, 30}

print(20 in a) #output:True
print(50 in a) #output:False


# Set Operations
'''
Operation	           Symbol	        Meaning	                                 Result
Union	               a | b	        All elements from both sets	            {1,2,3,4,5,6}
Intersection           a & b	        Common elements	                        {3,4}
Difference	           a - b	        Elements in A but not B	                {1,2}
Symmetricdifference	   a ^ b	        Elements in either set, but not both	{1,2,5,6}
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a&b)
print(a-b)
print(a^b)
print(a|b)


# Set Comprehension
a={x**3 for x in range(5)} #{0, 1, 64, 8, 27} set is unoredered proved
print(a)
a={x for x in "SDESowmyaSS"}
print(a)
a={x*2 for x in [1,2,34,4]}
print(a)
a={x*3 for x in (1,2,3,4,5,5)}
print(a)

a={x*3 for x in 78,9,89}  
print(a)
# a={x*3 for x in 78,9,89}
#                       ^
# SyntaxError: invalid syntax

# a={x*2 for x in 35556}
                    # ^^^^^
# TypeError: 'int' object is not iterable
"""



# Dictionaries in Python...................................

student = {
    "name": "Sowmya",
    "age": 19,
    "college": "AIT"
}

print(student)

# Access Values Using Keys
student = {
    "name": "SSS",
    "age": 19,
    "college": "AIT"
}
print(student['age'])


# Add or Update Values

student = {
    "name": "SSS",
    "age": 19,
    "college": "AIT"
}

student['age']=20
student['usn']="1ttt90"
print(student)


# Delete a Key-Value Pair
student = {
    "name": "SSS",
    "age": 19,
    "college": "AIT"
}

del student['age']  #using key value
print(student)


# get() Method

'''If a key doesn't exist, student["city"] raises a KeyError.

Use get() to avoid this error.'''

student = {
    "name": "SSS",
    "age": 19,
    "college": "AIT"
}
print(student.get('usn')) #None
print(student.get('usn',0)) #0


# Check Whether a Key Exists (in)
student = {
    "name": "SSS",
    "age": 19,
    "college": "AIT"
}
print('name' in student)#output:True
print('age' in student)#output:True



# Get All Keys
student = {"name": "Sowmya", "age": 19}

print(tuple(student)) #('name', 'age')
print(list(student))  #['name', 'age']


# Sort Dictionary Keys
student = {"zebra": 1, "apple": 2, "mango": 3}

print(sorted(student)) #output:['123', 'mango', 'zebra']


# Dictionary Comprehension
squares={x:x**2 for x in range(5)}
print(squares)

# Dictionary Unpacking (**)  Used to merge/collect/combine dictionaries.
a = {"name": "Sowmya"}
b = {"age": 19}
c={**a,**b}
print(c) #{'name': 'Sowmya', 'age': 19}


#methods

'''keys'''
student = {"zebra": 1, "apple": 2, "mango": 3}
print(student.keys())

'''values'''
student = {"zebra": 1, "apple": 2, "mango": 3}
print(student.values())

'''items'''
student = {"zebra": 1, "apple": 2, "mango": 3}
print(student.items())

student = {"zebra": 1, "apple": 2, "mango": 3}
x=(student.pop('zebra'))
print(x)   #output: 1
print(student)  #output:{'apple': 2, 'mango': 3}
'''pop() – Remove a key and return its value'''

'''update() – Add or update key-value pairs'''

student={
    "name":'sss','age':19
}
student.update({"age": 20, "course": "CSE"})

print(student)


'''
Dictionary Basics..
1.What is a dictionary?
2.Key-value pairs (key: value)
3.Creating a dictionary using {}.
4.Dictionaries are ordered (insertion order).
5.Keys must be unique.
6.Keys must be immutable/hashable.
Dictionary Operations..
7.Access values using keys: d["name"]
8.Add new key-value pairs.
9.Update existing values.
10.Delete using del.
11.Check key existence using in.
12.Get all keys using list(d) and sorted(d).
Important Dictionary Methods..
13. get() – Safely access a value.
14. keys() – Get all keys.
15. values() – Get all values.
16. items() – Get key-value pairs.
17. pop() – Remove a key and return its value.
18. update() – Add or update key-value pairs.
Advanced Concepts..
19.Dictionary unpacking (**).
20.Dictionary comprehension.
'''


# Looping Techniques..............................

'''1. items() – Loop through Dictionary'''
'''
student={
    "student":124,"studenta":345

}
for key,value in student.items():
    print(key,":",value)
'''

'''2. enumerate() – Get Index and Value'''
'''
fruits=["apple","banana","mango"]

for index,value in enumerate(fruits):
    print(index,value)'''
'''    
0 apple
1 banana
2 mango    '''

'''3. zip() – Loop Through Two Lists Together'''
'''name=("a","b")
age=(20,21)
for names ,ages in zip(name,age):
    print(names,ages)'''

'''4. reversed() – Loop in Reverse Order'''
'''number=[1,2,3,4,5,5]
for num in reversed(number):
    print(num)'''

'''sorted() – Loop in Sorted Order'''
'''number=[1,23,33,2,99]
for num in sorted(number):
    print(num)'''



'''6. set() + sorted() – Unique Sorted Elements'''
number=[3,5,6,66]
for num in (sorted(set(number))):
    print(num)

'''7. Create a New List While Filtering'''

# numbers = [10, 20, 30, 40, 50]
# result=[]
# for i in (numbers):
#     if i>20:
#         result.append(i)
# print(result)      

'''11. More on Conditions'''

'''1. Membership Operators
Check whether an element exists.'''

# a = [10, 20, 30]
# print(10 in a)
# print(10 not in a)


'''2. Identity Operators
is and is not check whether two variables refer to the same object.'''
# a=[10,20]
# a=b
# c=[10,20]
# print(a is b) #output:True
# print(a is not b) #output:False

'''3. Chained Comparisons
You can combine comparisons.'''


'''Operator	              Meaning
and	                   Both conditions must be True
or	                   At least one condition must be True
not	                   Reverses True/False'''


# age=19
# print(age>18 and age>19)
# print(age>18 or age>19)
# print(not age>18)



'''5. Short-Circuit Evaluation
Python stops checking when the result is already decided.'''

# print(False and True)
# print(True or False)


'''6. Walrus Operator (:=)
It assigns a value to a variable inside an expression.'''

# p=int(input())
# if (n:=p)>5:
#     print(p)


'''
| Topic                         | Concepts |
|---|---|
| Looping techniques             | `items()`, `enumerate()`, `zip()` |
| Reverse                        | `reversed()` |
| Sorting                        | `sorted()` |
| Unique elements                | `set()` |
| Membership                     | `in`, `not in` |
| Identity                       | `is`, `is not` |
| Comparisons                    | Chained comparisons |
| Boolean                        | `and`, `or`, `not` |
| Short-circuit                  | Stops when result is decided |
| Assignment expression/walrus operator          | `:=` |
'''


'''11. More on Conditions'''
'''1. Membership Operators – in and not in
Check whether an element exists in a collection.'''


# numbers = [10, 20, 30]
# print(20 in numbers)
# print(500 not in numbers)

'''2. Identity Operators – is and is not
Check whether two variables refer to the same object.'''
a = [10, 20]
b = a
c = [10, 20]

print(a is b) #output:True
print(b is a) #output:True
print(a is not c) #output:True
print(a is c) #output:False

'''3. Chained Comparisons
You can combine multiple comparisons in one statement.'''
a = 10

print(5 < a < 20)

'''Short-Circuit Returns a Value
 and  and or can return values other than True or False.'''
a = "" #this is empty string False
b = "Sowmya"
result = a or b
print(result)  #output:Sowmya
g="u"
f="jkkk"
result=g or f
print(result)   #output:u

a="yyyy"
b="gggg" 
print(a and b) #if all are true it returns true value
a=""
b="jkk"
print(a and b) #returns first false value
'''Operator	Rule
and	Returns the first False value; if all are True, returns the last value.
or	Returns the first True value; if all are False, returns the last value.'''

'''5.8. Comparing Sequences and Other Types'''
'''This section explains how Python compares lists, tuples and strings using <, >, and ==.'''

'''1. Lexicographical Ordering
Lexicographical means comparing items one by one from left to right.'''

a = (1, 2, 3)
b = (1, 2, 4)
print(a<b)


'''2. Same rule applies to lists'''
a = [10, 20, 30]
b = [10, 20, 40]

print(a < b)

'''3. Comparing strings'''
'''Python compares strings using Unicode values, not word meanings.'''
print("ABC" < "C")
print("Python" < "Pascal")
a=(1,3)
b=(1,5,7)
print(a<b)



'''4. Shorter sequence is smaller
If all elements match but one sequence ends earlier, the shorter sequence is smaller.'''
a=(10,20,30)
b=(1,25)
print(a>b) #output:True
 
a=(10,20)
b=(10,20,30)
print(a<b)  #output:True

'''5. Comparing integer and float values
Python can compare different numeric types.'''

print((1, 2, 3) == (1.0, 2.1, 3.0)) #output:False
print((1,2,3)==(1.0,2.000,3.0))#output:True

'''6. Comparing incompatible types'''
'''Python cannot directly compare unrelated types using < or >.'''
# print(10<"Hello") #output:TypeError
'''Because an integer and a string cannot be ordered against each other.'''
           
























 
