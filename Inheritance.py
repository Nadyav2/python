class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES send to {receipient} successful")
        else:
            print("You have insufficient funds to complete this transfer.")

class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_no):
        super().  __init__ (account_balance,phone_number)
        self.id_no =id_no
    def buy_airtime(self,amount):
        if self.account_balance>= amount:
           self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully.")

class Business_Mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_number):
        super().__init__ (account_balance,phone_number)
        self.business_number=business_number
    def receive_payment (self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")

personal=PersonalMpesa(2000,792392619,"4038743")
personal.send_money(300,79374759)
personal.buy_airtime(400)

personal=Business_Mpesa(4500,79865445,3456677)
personal.receive_payment(3000)
