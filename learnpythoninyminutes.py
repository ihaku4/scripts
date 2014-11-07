# Single line comments start with a hash.
"""	Multiline strings can be written
	using three "'s, and are often used
	as comments
"""

#######################################################
## 1. Primitive Datatypes and Operators
#######################################################

# You have numbers
3 #=> 3

# Math is what you would expect
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
5 / 2 #=> 2

# To fix division we need to learn about floats.
2.0		# This is a float
11.0 / 4.0 #=> 2.75 ahh...much better

# Enforce precedence with parentheses
(1 + 3) * 2 #=> 8

# Boolean values are primitives
True
False

# negate with not
not True #=> False
not False #=> True

# Equality is ==
1 == 1 #=> True
2 == 1 #=> False

# Inequality is !=
1 != 1 #=> False
1 != 2 #=> True

# More comparisons
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# Comparisons can be chained!
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too!
"Hello " + "world!" #=> "Hello world!"
"Hello " + 'world!' #=> "Hello world!"

# A string can be treated like a list of characters
"This is a string"[0] #=> 'T'

# % can be used to format strings, like this:
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
None #=> None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
"etc" is None #=> False
None is None #=> True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is 
# very useful when dealing with objects.

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
bool(0) #=> False
bool("") #=> False


#######################################################
## 2. Variables and Collections
#######################################################

# Python has a print function, available in versions 2.7 and 3...
print("I'm Python. Nice to meet you!")
# and an older print statement, in all 2.x versions but removed from 3.
print "I'm also Python!"


# No need to declare variables before assigning to them.
some_var = 5	# Convention is to use lower_case_with_underscores
some_var #=> 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# some_other_var	# Raises a name error

# if can be used as an expression
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1) 	# li is now [1]
li.append(2)	# li is now [1, 2]
li.append(4)	# li is now [1, 2, 4]
li.append(3)	# li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()		#=> 3 and li is now [1, 2, 4]
# Let's put is back
li.append(3)	#=> li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0] #=> 1
# Look at the last element
li[-1] #=> 3

# Looking out of bounds is an IndexError
# li[4] # Raises an IndexError
# li[-5] # Raises an IndexError

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
li[1:3] #=> [2, 4]
# Omit the beginning
li[2:] #=> [4, 3]
# Omit the end
li[:3] #=> [1, 2, 4]
# Select every second entry
li[::2] #=> [1, 4]
# print li[::2]
# Revert the list
li[::-1] #=> [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# dealing
# li + other_li
# li.extends(other_li)

# 1 in li
# len(li)


# Tuples
tup = (1, 2, 3)
tup[1]
a, b, c = (1, 2, 3)
d, e, f = 4, 5, 6
e, d = d, e


# Dictionaries
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
filled_dict["one"]

filled_dict.keys() #=> ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
filled_dict.values()
"one" in filled_dict
1 in filled_dict #=> False
# Looking up a non-existing key is a KeyError
# filled_dict["four"] # KeyError
#Use "get()" method to avoid the KeyError
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4
# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5) #filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6) #filled_dict["five"] is still 5
# print filled_dict["five"]



import math
# print dir(math)
# print math.sqrt(16)

d = DNSRecord.question("google.com")
print d