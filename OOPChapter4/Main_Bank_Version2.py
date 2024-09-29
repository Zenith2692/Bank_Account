# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the account class file
from Account import *

# Start off with an empty list of accounts
accountList = []

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountList.append(oAccount)
print("Mary's account number is 1")

accountList[0].show()
accountList[1].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts...')
accountList[0].deposit(50, 'JoesPassword')
accountList[1].withdraw(345, 'MarysPassword')
accountList[1].deposit(100, 'MarysPassword')

# Show the accounts
accountList[0].show()
accountList[1].show()

# Create another account with information from the user
print()
userName = input('What is the name for the new users account?')
userBalance = input('What is the starting balance for this account?')
userBalance = int(userBalance)
userPassword = input('What is the password you would like to set for this account?')
oAccount = Account(userName, userBalance, userPassword)
accountList.append(oAccount)

# Show the newly created account
print("Created new account, account number is 2")
accountList[2].show()

# Let's deposit 100 into the new account
accountList[2].deposit(100, userPassword)
userBalance = accountList[2].getBalance(userPassword)
print()
print("After depositing 100, the users balance is: ", userBalance)

# Show the new account
accountList[2].show()