def writelines():
    fo1 = open(r"D:\Rishith\Python\Unit_2\demo.txt",'w') 
    while True:
        line= input("Enter line : ")
        line+='\n'
        fo1.write(line)
        choice = input("Do you want to continue?(y/n) ")
        if choice == 'n':
            break
    fo1.close()

def lineread(fo2):
    sum = 0
    fo3 = fo2.read()
    for i in fo3.split():
        sum+=1
    return sum

writelines()
file = open(r"D:\Rishith\Python\Unit_2\demo.txt",'r')
print("The total no of words are : ",lineread(file))
file.close()
        
