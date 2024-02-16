class decreaseToOne:
    def __init__(self, n):
        self.start = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 0:
            x = self.start
            self.start -= 1
            return x
        else:
            raise StopIteration

myClass = decreaseToOne(10)
myiter = iter(myClass)

for x in myiter:
    print(x)