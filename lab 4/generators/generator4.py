# Exercise 4
def squares(a, b):
    for x in range(a, b + 1):
        yield x ** 2

myNums = squares(4, 11)
for x in myNums:
    print(x)


""" class squaresRange:
    def __init__(self, a, b):
        self.start = a
        self.end = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return (self.start - 1) ** 2
        else:
            raise StopIteration

mySquares = squaresRange(14, 20)
myiter = iter(mySquares)

for x in myiter:
    print(x) """