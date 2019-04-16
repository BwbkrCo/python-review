# WHILE Loop 

#Initializing our (empty) blockchain list
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction = [1] ):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    """ Returns the input of the user ( a new transaction amount) as a float.  """
    return float(input('Your transaction amount please: '))

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    #Output the blockchain list to the console. 
    # print(blockchain)
    for block in blockchain:
        print('Outputting Block')
        print(block)

# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount,get_last_blockchain_value())
    else:
        print_blockchain_elements()
    

    

print('Done!')