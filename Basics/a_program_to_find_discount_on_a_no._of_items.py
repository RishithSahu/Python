# A shop gives a  discount of 10%, if the cost of the quantity purchased is more than 1000 Ru, print total cost for the user.

quantity_of_items = int(input("Total no of items "))
cost = 100*quantity_of_items

if cost >= 1000:
    cost = cost - cost*0.1 
    print("The Grand total is ", cost)
else :
    print("The total price is ",cost)