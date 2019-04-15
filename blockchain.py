# print(2 + 2)

# Functions
# Define Code which is executed Later (and possibly Multple Times)
# def greet():
#     print('Hello')
# greet()
# greet()

blockchain = [1]

# def add_value():
#     blockchain.append([blockchain[-1],5.3])
#     print(blockchain)

# add_value()
# add_value()
# add_value()

########################################################################

# Functions
# Can receive Arguments
# def greet(name):
#     print('Hello ' + name)
# greet('Brian')

# def add_value(transaction_amount):
#     blockchain.append([blockchain[-1], transaction_amount])
#     print(blockchain)

# add_value(2)
# add_value(0)
# add_value(10.89)

###########################################################################

# Functions
# Can return Values
# def sum(a,b):
#     return a + b
# print(sum(2,5))

# blockchain = [[1]]

# def get_last_blockchain_value():
#     return blockchain[-1]

# def add_value(transaction_amount):
#     blockchain.append([get_last_blockchain_value(), transaction_amount])

# add_value(2)
# add_value(0.9)
# add_value(10.89)

# print(blockchain)

#############################################################################################

# Functions
# Default Arguments
# def greet(name, age=30):
#     print('Hello ' + name + ', I am ' + age)
# greet('Brian')

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1]

# def add_value(transaction_amount, last_transaction = [1] ):
#     blockchain.append([last_transaction, transaction_amount])

# add_value(2)
# add_value(0.9, get_last_blockchain_value())
# add_value(10.89,get_last_blockchain_value())

# print(blockchain)

################################################################################################

# Functions
# Keyword Arguments (kwargs)
# def greet(name, age):
#     print('Hello ' + name + ', I am ' + age)
# greet(age = 30, name = "Brian")

blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction = [1] ):
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    """ Returns the input of the user ( a new transaction amount) as a float.  """
    return float(input('Your transaction amount please: '))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount,get_last_blockchain_value())

print(blockchain)

####################################################################################################

# Variable Scope

# Global Scope
# name = 'Brian
# def greet():
#     print('Hi' + name)
# greet()

# Local Scope
# name = 'Brian'
# def greet():
#     age = 30
#     print('Hi ' + name + ", I am " + age)
# greet()