# WAP to generate first 1 lakh values.
def gen2(i):
    while i<=100000:
       yield i
       i+=1
g = gen2(1)
while True:
   print(next(g))