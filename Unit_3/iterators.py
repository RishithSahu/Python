class mycontainer:
    def __init__(self,mylst):
        self.mylst = mylst
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i <= len(self.mylst):
            return self.mylst[self.i-1]
        else:
            raise StopIteration
        
a = [1,2,3,4,5]
c = mycontainer(a)
for i in c:
    print(i)