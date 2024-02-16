class printDiv:
    def __init__(self, n):
        self.num = 1
        self.stop = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.num + 12 <= self.stop:
            self.num += 12
            return self.num
        else:
            raise StopIteration

myNum = printDiv(60)
myiter = iter(myNum)

for x in myiter:
    print(x)