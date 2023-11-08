n = int(input("Enter number of elements: "))

input_lst = []

for i in range(n):
    input_lst.append(int(input("Enter a digit: ")))

k = int(input("Enter frequency to delete: "))

for item in set(input_lst):
    if input_lst.count(item) == k:
        input_lst = [j for j in input_lst if j != item]

print(f"Output = {input_lst}")