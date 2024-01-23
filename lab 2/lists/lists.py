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