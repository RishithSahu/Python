n = int(input("Enter a number: "))
sett = {1,2}
for i in range(2,n):
    x = "True"
    for j in range(2,i+1):
      if i==2:
          break
      elif i%j==0:
          x = "False"
      elif x == "True":
          sett.add(i)

print(sett)