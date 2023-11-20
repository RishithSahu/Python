import csv

def read_csv():
    with open("D:\Rishith\Python\Mini Project\Library_Database_ISBN.csv",'r') as file1:
        r = csv.reader(file1)
        data = list(r)
        for row in data:
            for col in row:
              return (col)

def csv_values():
   with open("D:\Rishith\Python\Mini Project\Library_Database_ISBN.csv",'r') as file1:
        r = csv.reader(file1)
        data = list(r)
        print(data)
        for i in data:
            print(len(data))
            return i
          
print(csv_values())