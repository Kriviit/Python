class ATM:
    def __init__(self,name,account_number,phone_number,pin,initial_balance):
        self.account_number=account_number
        self.phone_number=phone_number
        self.pin=pin
        self.name=name 
        self.total_balance=initial_balance
    
    def isAuthorized(self,account_number,pin):
        return account_number==self.account_number and pin==self.pin
    
    def withDraw(self,account_number,pin,amount):
        if self.isAuthorized(account_number,pin):
            if self.total_balance>=amount:
                self.total_balance=self.total_balance-amount
                print(amount)
            else:
                print( "insufficent balance")
        else:
            print( "account no or pin is invalid")

    def changePin(self,account_number,pin,new_pin):
        if self.isAuthorized(account_number,pin):
            self.pin=new_pin
            print("pin as changed")
        else:
            print("account no or pin is invalid")

    def checkBalance(self,account_number,pin):
        if self.isAuthorized(account_number,pin):
            print("current balance",self.total_balance)
        else:
            print("account no or pin is invalid")

pavan=ATM("Pavan",1001,98734123748,2000,5000)
harika=ATM("Harika",1002,98734123748,2000,50000)

pavan.checkBalance(1001,2000)
harika.withDraw(1002,2000,5000)
harika.checkBalance(1002,2000)