class ATM :
    def __init__ (self, currentAmt, withdrawalAmt, addAmount):
        self.currentAmt = currentAmt
        self.withdrawalAmt = withdrawalAmt
        self.addAmount = addAmount
    
    def addMoney(self):
        print('Current Money = ', self.currentAmt)
        print('Money to be added = ', self.addAmount)
        print('Total Money = ', self.currentAmt + self.addAmount)

    def withdrawMoney(self):
        print('Current Money = ', self.currentAmt)
        print('Money to be withdrawn = ', self.withdrawalAmt)
        print('Total Money = ', self.currentAmt - self.withdrawalAmt)
    
    def currentMoney(self):
        print('Current Money = ', self.currentAmt)



current = int(input('Enter Current Amount : '))
add = int(input('Enter amount to be added : '))
remove = int(input("Enter amount to be removed : "))

transaction = ATM(current, remove, add)


toDo = int(input('Do you want to ADD(1) or WITHDRAW(2) or view CURRENT(3)? Enter the respective number.'))
if toDo == 1:
    transaction.addMoney()

elif toDo == 2:
    transaction.withdrawMoney()

elif toDo == 3:
    transaction.currentMoney()
else:
    print('No function exists for that number. Please try again and enter a valid number.')