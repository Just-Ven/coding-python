# Exercise 2
class printEvenNums:
    def __init__(self):
        self.even = 0
        self.stop = int(input('Enter some number n: '))

    def __iter__(self):
        return self

    def __next__(self):
        if self.even <= self.stop:
            self.even += 2
            return self.even
        else:
            raise StopIteration

myEven = printEvenNums()
myiter2 = iter(myEven)

for x in myiter2:
    print(x, end=", ")