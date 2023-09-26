# Sum of n numbers using for loop but decrement counter.
n = int(input())
sum =  0
for i in range(n,0,-1):
    sum = sum + i
print(sum)