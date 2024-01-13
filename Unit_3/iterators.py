class mycontainer:
    def __init__(self,mylst):
        self.mylst = mylst
    def __iter__(self):
        self.i = 1
        return self
    def __next__(self):
        if self.i <= len(self.mylst):
            return self.mylst[::-(self.i)]
        else:
            raise StopIteration
        
a = [1,2,3,4,5]
c = mycontainer(a)
for i in c:
    print(i)