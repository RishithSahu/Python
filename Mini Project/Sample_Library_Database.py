import csv

NrowBOOK = int(input("Enter number of books in database: "))
NrowSTD = int(input("Enter number of students: "))
print()

#Open and write to the csv file bookmaster
with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Bookmaster.csv",'a') as bookmaster:
  csvwriter = csv.writer(bookmaster) #Creating a csv writer object
  csvwriter.writerow(["SL NO.", "ISBN", "TITLE", "AUTHOR", "AVAILABILITY"])
  sl_no = 0
  BKKrow = []
  for i in range(NrowBOOK):
    sl_no += 1
    copies = "Available"
    ISBN = input("Enter book ISBN: ")
    title = input("Enter book title: ")
    author = input("Enter author: ")
    with open("D:\Rishith\Python\Mini Project\Library_Database_ISBN.csv",'r') as file1:
      r1 = csv.reader(file1)
      data1 = list(r1)
      for i in data1:
        for j in i:
          if j == ISBN:
            copies = "Borrowed"
            break
      if copies != "Borrowed":
         copies = "Available"
    x = [sl_no, ISBN, title, author, copies]
    BKKrow.append(x)
    print()
  csvwriter.writerows(BKKrow)
  print("Database Bookmaster Created.")

#Open and write to the csv file studentmaster
with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Studentmaster.csv",'a') as studentmaster:
  csvwriter = csv.writer(studentmaster) #Creating a csv writer object
  csvwriter.writerow(["SL NO.", "SRN", "NAME", "CARD NUMBER", "BOOKS BORROWED"])
  sl_no = 0
  STDrow = []
  for i in range(NrowSTD):
    sl_no += 1
    borrowed = 0
    SRN = input("Enter student SRN: ")
    name = input("Enter student name: ")
    card = int(input("Enter card number: "))
    with open("D:\Rishith\Python\Mini Project\Library_Database_SRN.csv",'r') as file2:
      r2 = csv.reader(file2)
      data2 = list(r2)
      for i in data2:
        for j in i:
          if j == SRN:
            borrowed += 1
        class Book_Record:
          def __init__(self,sl_no, SRN, name, card, borrowed):
            self.S_no = sl_no
            self.SRN = SRN
            self.name = name
            self.card = card
            self.borrowed = borrowed
    x = [Book_Record(sl_no, SRN, name, card, borrowed)]
    STDrow.append(x)
    print()
  csvwriter.writerows(STDrow)
  print("Database Studentmaster Created.")













