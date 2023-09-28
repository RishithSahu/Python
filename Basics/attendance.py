# If student attendance is greater than 80 then print hallticket.
attendance = int(input("No. of days present "))
conduct = input("Conduct ")
year = int(input("Which year?"))
if attendance >= 80 and  conduct == 'good' :
    print("Hallticket")
if year == 2023:
    print("Be issued an hallticket.")