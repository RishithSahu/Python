
testcases = int(input())
lst = []
lst2 = []


for i in range(testcases):
    lst = input().split()

    for j in range(len(lst)):
       lst[j] = int(lst[j])

    if lst[0] > lst[1]:
       lst2.append(lst[0])
    elif lst[1] >= lst[0]:
       lst2.append(lst[1])
    else:
       continue
for j in range(len(lst2)):
    print(lst2[j])