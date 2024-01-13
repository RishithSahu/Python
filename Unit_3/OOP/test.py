class sample:
   def __init__(self,m,n,o):
        self.a=m
        self.b=n
        self.c=o
class sample_child(sample):
    def __init__(self,m,n,o,q):
        super().__init__(m,n,o)
       #sample.__init__(self,m,n,o)
        self.e=q
    def display(self):
        print(self.a,"--",self.b,"--",self.c,"--",self.e)
s1=sample_child(1,2,3,4)
s1.display()
