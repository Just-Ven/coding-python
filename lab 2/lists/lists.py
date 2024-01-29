# Example 1
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Example 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Example 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Example 5
list1 = ["abc", 34, True, 40, "male"]

# Example 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # class 'list'


# Example 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Example 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Example 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Example 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Example 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Example 6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Example 7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Example 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 3
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Example 4
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Example 1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# example 3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Example 4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Example 3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Example 4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # removes the last item in the list

# Example 5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Example 6
thislist = ["apple", "banana", "cherry"]
del thislist # delete list completely

# Example 7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # пустой список


# Example 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Example 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Example 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Example 4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Example 3
#newlist = [expression for item in iterable if condition == True]; short syntax for looping lists

# Example 4
newlist = [x for x in fruits if x != "apple"]

# Example 5
newlist = [x for x in fruits] # with no if condition

# Example 6
newlist = [x for x in range(10)]

# Example 7
newlist = [x for x in range(10) if x < 5]

# Example 8
newlist = [x.upper() for x in fruits]

# Example 9
newlist = ['hello' for x in fruits]

# Example 10
newlist = [x if x != "banana" else "orange" for x in fruits]


# Example 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Example 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Example 3
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Example 4
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # сортирует по разнице n - 50

# Example 5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Example 6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # сортировка без учета регистра

# Example 7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# Example 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Example 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# Example 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Example 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # join 2 lists by using loops

# Example 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''
Lists methods:
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

# Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Example 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# Example 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Example 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Example 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Example 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
