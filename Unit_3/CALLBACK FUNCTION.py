#                                 CALLBACK FUNCTION
   
'''
   A function will return a function.
'''
def calc(a,b):
    operator = input("What operation do you want to do ? ")
    if operator == "a":
        return a+b                                # It would be better to have a  
    elif operator == "m":                  # function if the code is too big.
        return a*b
    elif operator == "s":
        return a-b
    elif operator == "d":
        return a/b
    else:
        return "Invalid operator"
    
print(calc(12,34))