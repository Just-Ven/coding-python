# Examples 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Examples 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # in typles allowed duplicates

# Examples 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Example 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Example 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Example 5
tuple1 = ("abc", 34, True, 40, "male")

# Example 6
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Example 7
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Example 2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Example 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Example 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# Examples 5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Example 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Example 2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Example 3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Example 4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Example 5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# Example 1
fruits = ("apple", "banana", "cherry") # packing a tuple

# Example 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Example 3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # using asterisk

# Example 4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Example 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Example 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Example 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# Example 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Example 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

'''
Tuples method:
Method	Description

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

# Exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])