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





#ChainMap objects¶
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



