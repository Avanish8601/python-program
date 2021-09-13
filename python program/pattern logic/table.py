class Table:

    def __init__(self,n):
        self.n=n
    def __iter__(self):
        self.i=0
        return self
    def __next__(self):
        self.i+=1
        if self.i>10:
            raise StopIteration
        value=self.n * self.i
        return value
t1=Table(3)
for i in t1:
    print(i)


