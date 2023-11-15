str = input("Enter String")

half = len(str)/2

first_half = str[:half]
second_half = str[half:]
reverse_second_half = second_half[::-1]

if first_half == second_half:
    print("It is Symmetrical")
elif first_half == reverse_second_half:
    print("It is a Palindrome")