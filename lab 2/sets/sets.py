# Example 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Examples 2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # in sets duplicates are not allowed

# Examples 3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # True and 1 is considered as same value

# Examples 4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) # False and 0 is considered as same value

# Examples 5
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Examples 6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Examples 7
set1 = {"abc", 34, True, 40, "male"}

# Examples 8
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>

# Examples 9
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>

# Examples 10
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Example 1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Example 2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.


# Example 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Example 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Example 3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Example 1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Example 2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Example 3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) # will be deleted random element of the set

# Example 4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # will clear the set

# Example 5
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # will completely delete the set


# Example 1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# Example 1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Example 2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Example 3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) # will print only same elemts in both sets

# Example 4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) # Return a set that contains the items that exist in both set x, and set y:

# Example 5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# Example 6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) # Return a set that contains all items from both sets, except items that are present in both:

# Example 7
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z) # True and 1 is considered the same value:


'''
Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''

# Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

