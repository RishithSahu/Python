'''                                           DICTIONARY
Data is stored as a key and value pair
                (Imutable) (Mutable)
dic = {1:'2fvfrrr3',2:'3wwsww'}  
'''

dic = {1:'one fellow',2:'two fellow',3:'three fellow',4:'four fellow',5:'five fellow'}
print(dic[1])
print(type(dic))
print(dic.items())
print(dic.keys())
print(dic.values())

employee = {}
for i in range(1):
    name = input("Enter name ")    # The name has to be name
    salary = input("Enter Salary ")
    employee[name] = salary
print(employee)

for ele in employee.items():
    print(ele)
     
print(employee.get(name))