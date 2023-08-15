from BankAccount import *


def main():
    
#Ask user for the number of transactions.
    account = BankAccount()
    count = int(input("How many transtractions would you like to make ? "))
    transnum = 0 



#	For each transaction ask for type of transaction and amount of transaction.
#	If type of the transaction is withdarw then use the withdraw method to complete the transaction. If return value from the withdraw method is False, then display an error message.
    for i in range(count):
        Type = input("enter transaction type: ")
        amount = float(input("Enter transaction amount: "))
        if Type == 'deposit':
            if (account.deposit(amount)):
                transnum += 1
                print('transaction was successful, your balance is:', '{0:.2f}'.format(account.getBalance()))
            else:
                print("Deposit amount is less than 0 ")
                print("transaction rejected: ")
        else:
            if (account.withdraw(amount)):
                transnum += 1
                print("transaction was successful")
            else:
                print(amount , "is higher than", '{0:.2f}'.format(account.getBalance()))
                print("transaction rejected")
        print('your balance is: {0:.2f}'.format(account.getBalance()), "number of transations", transnum)
#	If type is deposit, then use deposit method to complete the transaction. If return value from the deposit method is False, then display an error message.
   
#	After the loop display the number of transactions completed and account balance. If any transaction is rejected, then it will not be included in the count of completed transactions.
