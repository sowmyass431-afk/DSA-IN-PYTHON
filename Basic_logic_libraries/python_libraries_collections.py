'''The official Python documentation is saying that collections is a module containing special data structures. These are alternatives to normal Python list, dict, set, and tuple.

Here is what each one means:

Name	                           Simple meaning

namedtuple()	                  Tuple with named fields
	             
ChainMap	                      Combine multiple dictionaries into one view

deque	                           Add/remove elements quickly from both ends
	
Counter	                           Count how many times elements appear	High

OrderedDict	                       Dictionary that remembers insertion order

defaultdict	                       Dictionary with automatic default values	

UserDict	                       Wrapper around dictionaries
	
UserList	                       Wrapper around lists
	
UserString	                       Wrapper around strings'''





#ChainMap objects¶..................................
# ChainMap combines multiple dictionaries into one view without creating a new combined dictionary.
from collections import ChainMap

student = {"name": "Sowmya", "age": 19}
college = {"name": "A", "course": "CSE"}

data = ChainMap(student, college)

print(data["name"])    # Sowmya
print(data["course"])  # CSE

'''Important: If the same key exists in multiple dictionaries, ChainMap takes the value from the first dictionary.'''

# 2. Three important concepts
'''
A. Lookup

It searches dictionaries from first to last.

print(data["course"])

It finds "course" in the second dictionary.'''
'''
B. Update

Changes happen only in the first dictionary.
data["age"] = 20


This updates student, not college.
C. Reference

If you change an original dictionary, ChainMap reflects that change.'''
'''
3. Methods to understand
Feature	                Meaning

maps	           Shows the dictionaries

new_child()	       Adds a new dictionary at the beginning

parents	           Returns a ChainMap without the first dictionary'''


'''Examples'''

'''MAP'''
from collections import ChainMap
student={"name":"SSS"}
college={"course":"CSE"
}
data=ChainMap(college,student)
print(data)
#output:ChainMap({'course': 'CSE'}, {'name': 'SSS'})

print(data.maps) #[{'course': 'CSE'}, {'name': 'SSS'}]


# 2 new_child() — Add a new dictionary at the beginning

new_data=data.new_child({"NAME":"C"})
print(new_data)
#ChainMap({'NAME': 'C'}, {'course': 'CSE'}, {'name': 'SSS'}

#3. parents — Skip the first dictionary

parent_data=new_data.parents
print(parent_data) 
#ChainMap({'course': 'CSE'}, {'name': 'SSS'})


# '''ChainMap Examples and Recipes'''....

# 1. Python's internal lookup chain
import builtins
pylooks=ChainMap(locals(),globals(),vars(builtins))
'''
Python searches for a variable in three places:
1. locals() – current local variables.
2. globals() – global variables.
3. vars(builtins) – built-in names such as print(), len().
Purpose: Demonstrates how multiple levels of variable lookup can be combined.
'''

# 2. Command-line arguments, environment variables and defaults
'''
Imagine an application has three possible sources for its settings:
- Command-line arguments
- Environment variables
- Default values
Why blue? Because the first dictionary has higher priority.

Purpose: Choose settings according to priority.'''

defaults = {'color': 'red', 'user': 'guest'}

command_line_args = {'color': 'blue'}

combined = ChainMap(defaults,command_line_args) 

print(combined['color'])  # red
print(combined['user'])   # guest

combined = ChainMap(command_line_args,defaults) 
print(combined['color']) #blue



'''3. Nested contexts (updating values)
Imagine dictionaries representing different levels:
from collections import ChainMapc = ChainMap()d = c.new_child()e = c.new_child()'''

from collections import ChainMap

d1={"1":"A","2":"B"}
d2={"3":"c","4":"D"}
c=ChainMap(d1,d2)
d=c.new_child({"5":"E"})
e=c.new_child({"6":"F"})
print(d.maps)
print(e.maps)
c["1"]="d"
c["2"]="c"
'''
output:
[{'5': 'E'}, {'1': 'A', '2': 'B'}, {'3': 'c', '4': 'D'}]
[{'6': 'F'}, {'1': 'A', '2': 'B'}, {'3': 'c', '4': 'D'}]
'''
'''
Here:
- c = root context.
- d = one child context.
- e = another child context.
Each child has its own first dictionary but can look up values in its parent context.

Purpose: Understand nested scopes and contexts.'''

# 4. DeepChainMap
'''
This is an advanced custom class built by inheriting from ChainMap.

Normal ChainMap:
- Updates only the first dictionary.
- Deletes only from the first dictionary.



DeepChainMap changes this behaviour:
- Updates a key wherever it is found.
- Deletes a key wherever it is found.
- Adds new keys to the first dictionary.
Purpose: Customise how dictionary updates and deletions work.'''



'''Examples'''
#1.Student Information'''
from collections import ChainMap
student={"Name":12,"age":3}
studenta={"A":122,"B":7889}
data=ChainMap(student,studenta)
print(data["A"]) #output:122
print(data["age"])  #output:3

# Example 2: Priority of values

from collections import ChainMap

user_settings = {"color": "blue"}
default_settings = {"color": "red", "language": "English"}

settings = ChainMap(user_settings, default_settings)

print(settings["color"])
print(settings["language"])

# Example 3: Updating values
from collections import ChainMap
first={"a":10,"b":20}
second={"c":30,"d":40}
data=ChainMap(first,second)
data["a"]=50
data["e"]=40
print(data.maps)

# Example 4: new_child()
from collections import ChainMap
student1={"name":"SSS","age":19}
student2={"name":"yyy","age":19}
data=ChainMap(student1,student2)
new_data=data.new_child({"sem":14})
print(new_data["age"])
print(new_data.maps)
#output:
# 19
# [{'sem': 14}, {'name': 'SSS', 'age': 19}, {'name': 'yyy', 'age': 19}]


# Example 5: parents
# parents skips the first dictionary in the chain.
from collections import ChainMap
first={"a":10}
second={"b":20}
third={"c":30}
data=ChainMap(first,second,third) 
parents_data=data.parents
print(parents_data.maps)
print(data.maps)

#output:
'''
[{'b': 20}, {'c': 30}]
[{'a': 10}, {'b': 20}, {'c': 30}]'''



#counter ⭐................................
# 1. Understand Counter
# Counter counts how many times each element appears.
from collections import Counter
numbers=[1,3,3,4,4,5,6,6,6,7,8,89,90]
result=Counter(numbers)
print(result) 
print(result[3]) #output:2
#output:Counter({6: 3, 3: 2, 4: 2, 1: 1, 5: 1, 7: 1, 8: 1, 89: 1, 90: 1})

# 2. most_common() — Find frequent elements
from collections import Counter
numbers=[1,3,3,4,4,5,6,6,6,7,8,89,90]
count=Counter(numbers)
most_num=count.most_common()
print(most_num)
#output:[(6, 3), (3, 2), (4, 2), (1, 1), (5, 1), (7, 1), (8, 1), (89, 1), (90, 1)]
most_num=count.most_common(2)
print(most_num) #output:[(6, 3), (3, 2)]


# 3. elements() — Repeat elements according to counts
from collections import Counter
counts=Counter(a=3,abc=5,abcd=7)
result=list(counts.elements())
print(result)
#output:['a', 'a', 'a', 'abc', 'abc', 'abc', 'abc', 'abc', 'abcd', 'abcd', 'abcd', 'abcd', 'abcd', 'abcd', 'abcd']

# 4. update() — Add counts

from collections import Counter

count=Counter(['apple','banana','apple'])
print(count)
#output:Counter({'apple': 2, 'banana': 1})
#update-adding to old one
count.update(['orange','apple'])
print(count)
#output:Counter({'apple': 3, 'banana': 1, 'orange': 1})


# 5. subtract() — Subtract counts
from collections import Counter
count=Counter(a=3,b=7)
count.subtract(Counter(a=4,b=5))
print(count)
#output:
# Counter({'b': 2, 'a': -1})

# 6. total() — Sum all counts
from collections import Counter
count=Counter(a=3,b=7)
print(count.total())
#output:10


#deque............................................................
'''deque means Double-Ended Queue (pronounced "deck").

It is a data structure that allows us to:
- Add elements at the beginning.
- Add elements at the end.
- Remove elements from the beginning.
- Remove elements from the end.

Understand with an example
Imagine a queue:
FRONT → [10] [20] [30] [40] ← REAR

With a normal list, removing the first element (pop(0)) requires shifting the remaining elements.

With deque, adding and removing from either end is approximately O(1) — very efficient.

'''

# 2. Import and create a deque
from collections import deque
numbers=deque([1,2,3,4,4])
print(numbers)
#output:deque([1, 2, 3, 4, 4])
# You can also create an empty deque:
# numbers = deque()


'''
| Method        |        Meaning        |        Priority        |
|            ---|---     ---            |
| `append()`            | Add at right  | Must learn      |
| `appendleft()`        | Add at left    | Must learn     |
| `pop()`            | Remove from right   +| Must learn |
| `popleft()`      | Remove from left      | Must learn |
| `extend()`      | Add multiple elements at right      | M     ust learn |
| `extendleft()`      | Add multiple elements at left   | Must learn |
| `rotate()`        | Rotate elements                   | Must learn |
| `clear()`         | Remove all elements               | Learn      |
| `count()`         | Count occurrences                 | Learn      |
| `index()`         | Find position                     | Learn      |
| `insert()`        | Insert at a position              |   Later    |
| `remove()`        | Remove first matching value        | Learn     |
| `reverse()`       | Reverse elements                   |  Learn     |
| `copy()`          | Create a shallow copy              | Later      |'''



# 4. Let's start practising: append()
from collections import deque
numbers=deque([1,2,3,4,5,6,7,8,8])
numbers.append(10)
print(numbers) #output:deque([1, 2, 3, 4, 5, 6, 7, 8, 8, 10])
numbers.appendleft(11)
print(numbers) #output:deque([11, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10])

# 5. pop() — Remove from the right side

# pop() removes the last element from a deque and returns that element.

from collections import deque
numbers=deque([1,2,3,4,4,5,6,6,7,7,8,8,8])
n=numbers.pop()
print(n) #it will return
print(numbers)
#output:deque([1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8])
#output:8

#popleft.
n=numbers.popleft()
print(numbers)
print(n)
#output:
# deque([2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8])
# 1

# 6.extend() — Add multiple elements at right

from collections import deque
numbers=deque([1,2,3,4,5])
numbers.extend([10,20,30])
print(numbers)
#output:deque([1, 2, 3, 4, 5, 10, 20, 30])

# extendleft....
# extendleft() — Add multiple elements at left
from collections import deque
numbers=deque([1,2,3,4,5])
numbers.extendleft([10,20,30])
print(numbers)
# deque([30, 20, 10, 1, 2, 3, 4, 5])

#7.clear
from collections import deque
numbers=deque([1,2,3,4,5])
numbers.clear()
print(numbers)
#output:deque([])


# 8 count() — Count occurrences

from collections import deque
numbers=deque([1,2,3,4,5,5,5,5])
n=numbers.count(5)
print(n)
#output:4

# 10 index() — Find the position
from collections import deque
numbers=deque([1,2,3,4,5,5,5,5])
n=numbers.index(5)
print(n)

#11 insert() — Insert at a position
from collections import deque
numbers=deque([1,1,3,4,5,6,7,8])
numbers.insert(1,100)
print(numbers)
#output:deque([1, 100, 1, 3, 4, 5, 6, 7, 8])

# 12 remove() — Remove first matching value
from collections import deque
numbers=deque([1,1,3,4,5,6,7,8])
numbers.remove(1)
print(numbers)
#output:deque([1, 3, 4, 5, 6, 7, 8])


# 13 . reverse() — Reverse elements

from collections import deque
numbers=deque([1,1,3,4,5,6,7,8])
numbers.reverse()
print(numbers)
#output:eque([8, 7, 6, 5, 4, 3, 1, 1])

# 14 rotate() — Rotate elements..

# This is an important deque method.

# A. Rotate right
from collections import deque
numbers=deque([10,20,40,1,2,3])
numbers.rotate(1)
print(numbers)
#output:
# deque([3, 10, 20, 40, 1, 2])

#B.Rotate Right
from collections import deque
numbers=deque([10,20,30,40,1,3,4])
numbers.rotate(2) #output:deque([3, 4, 10, 20, 30, 40, 1])
print(numbers)
#output:
numbers.rotate(-1)
print(numbers)
# deque([20, 30, 40, 1, 3, 4, 10])

#15. copy() — Create a copy
from collections import deque
numbers=deque([1,33,4,4,5,6])
new_number=numbers.copy()
print(new_number)
#output:
# deque([1, 33, 4, 4, 5, 6])


