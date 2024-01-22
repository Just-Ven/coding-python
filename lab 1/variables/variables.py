# Examples
x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a




# Exercise 1
carname = 'Volvo'

# Exercise 2
x = 50

# Exercise 3
x = 5
y = 10
print(x + y)

# Exercise 4
x = 5
y = 10
z = x + y
print(z)

# Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

# Exercise 6
x = y = z = 'Orange'

# Exercise 7
def myFunc():
    global x
    x = 'fantastic'