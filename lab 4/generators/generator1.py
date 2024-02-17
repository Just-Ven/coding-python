# Exercise 1
def printSquares(n):
    for x in range(n + 1):
        if x ** 2 < n:
            yield x ** 2
        else:
            break

myNums = printSquares(5)
for x in myNums:
    print(x)


""" class squaresOfNumbers:
    def __init__(self, n):
        self.stop = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num ** 2 <= self.stop:
            self.num += 1
            return (self.num - 1) ** 2
        else:
            raise StopIteration

myNum = squaresOfNumbers(100)
myiter = iter(myNum)

for x in myiter:
    print(x) """