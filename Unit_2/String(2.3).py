# Makes UPPERCASE and lowercase(and checks if true or false) 
s3 = "PYTHON"
s1 = "1234"
print(s3.lower())
print(s3.isupper())

print(s3.upper())
print(s3.islower())
# Capitalise makes only first letter capital

print(s3.isalpha()) # Alphabet
print(s3.isalnum()) # Numeric
print(s1.isdigit()) # Digit in the form of a string(At least one charecter)

print(4*s3)
print("1234 "+s3.lower+" Is The best bro!!")
# isspace()    Will check if there is only space
print(s3.ljust(30,'#'))
print(s3.rjust(30,'#'))
print(s3.center(30,' '))