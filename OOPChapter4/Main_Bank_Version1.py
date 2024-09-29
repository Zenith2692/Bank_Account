# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the account class file
from Account import *

# Create two accounts
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Account created for Joe')

oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print('Account created for Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for the new users account?')
userBalance = input('What is the starting balance for this account?')
userBalance = int(userBalance)
userPassword = input('What is the password you would like to set for this account?')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created account
oNewAccount.show()

# Lets deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print("After depositing 100, the users balance is: ", userBalance)

# Show the new account
oNewAccount.show()