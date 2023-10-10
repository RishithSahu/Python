# Q10 Create list of numbers 1 to n exept n/2.

list = []
n = int(input("type n "))   

for i in range(n):
    if (i == n/2):
        continue
    else:
      list.append(i)
print(list)
