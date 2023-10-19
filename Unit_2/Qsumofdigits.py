# WAP using a function to find sum of digits of a number n. The functin should return the sum a default value of 1,2,# 3,4,5 if value not supplied.
print("H")

def sum_of_digits(n):
    sum = 0
    while n>0:
        r=n%10
        sum+=r
        n=n//10
    return sum

n = int(input("Enter the number "))
ans = sum_of_digits(n)
print(ans)