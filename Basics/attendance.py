# If student attendance is greater than 80 then print hallticket.
attendance = int(input("No. of days present "))
conduct = input("Conduct ")
year = int(input("Which year?"))
if attendance >= 80 and  conduct == 'good' :
    print("Hallticket for",year)
else:
    print("Attendace is less or conduct is not good Hallticket cannot be issued")
