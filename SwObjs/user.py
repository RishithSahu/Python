# A User object.
class User:
    def __init__(self,name,address,ph_no):
        self.username = name
        self.address = address
        self.Phone_No = ph_no


class Transactions:
    def __init__(self,Date_Value_Date,narration,debit,credit,total_balance):
        self.Date = Date_Value_Date
        self.Narration = narration
        self.Debit = debit
        self.Credit = credit
        self.Total_Balance = total_balance
        
class Account_Details:
    def __init__(self,acc_no,totalbalance,unclearbal,MODbal,currency):
        self.Account_number = acc_no
        self.Total_Balance = totalbalance
        self.Uncleared_balance = unclearbal
        self.MOD_Balance = MODbal
        self.Currency = currency