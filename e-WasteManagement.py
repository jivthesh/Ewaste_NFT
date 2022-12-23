'''
WORKING PROCESS:
1. start with new user---> new
enter only the account number 0-9 to select the address
(0) 0x2376c5611f8d6cd9d4d2ca0d1e066e3027dc0a28

(1) 0x88027b70475b434fce64eab664a37248aa6fe378
(2) 0x0b46d22501384ed9b65f873d45797a9f174f5dc4
(3) 0x0ffaae39150264b9bf2585aec33e47f7bc8cd5ec
(4) 0xdbf765eaa87889eda8e57250f70902eea444925b
(5) 0x0221376c94f143516979997b4d7cf9d6a081d5de
(6) 0xda068b1d07a41fdeade9a17d6b61aec9a6b29755
(7) 0xcd01bba398909963331393cbed7f0b20c5737390
(8) 0x3e0d65d39fde578afe75873cfd1fa5469295ad79
(9) 0x4fa9ac5430d1c29a12b4ca54685740795038f08b
add random ID(not linked and can be any number for now) and user name

2. From the selection option next ---> user
enter the user account that has been used for creating new user(other account wont work)
Questions are not added, but each question takes 1 for true and 0 for false

3. From the the selection option next ---> validator
enter the same user account previously used for option user
answer the question with 1 / 0 for the questions

4. from the selection option next ---> compare
enter the same user account previously used for option user

ISSUE:
call()---> working but not changing state
transact() ---> error

'''

import json
from web3 import Web3, HTTPProvider 



def newUser(address):
    #print(address)
    addno = int(input("Enter the account number(1-9) :"))
    new_address = address[addno]
    userid = int(input("enter the user id :"))
    name = str(input("Enter the user name :"))
    res = contract.functions.newUser(new_address,userid,name).transact()
    if res:
        print("\n--- new address added to the chain ---\n")
        return new_address

def comparePoints(address):
    ipt_address = input("Enter the User address to compare the scores :")
    if ipt_address in address:
        a = contract.functions.mappValueUser(ipt_address).call()
        b = contract.functions.mappValueValidator(ipt_address).call()
        print(f'\nUser score :{a}')
        print(f'Validator score :{b}')
        res = contract.functions.compare(ipt_address).call()
        # print(res)
        if res:
            print("\n--- The product is validated!! proceed to collect the E-waste ---")
        else:
            print("\n--- product mark differ and not eligible for the estimated token ---")


def validator(address):
    ipt_address = input("Enter the User address to validate :")
    if ipt_address in address:
        print("\nBased on the questions award 1/0 points")
        for i in range(1,6):
            pt = int(input(f'question {i}: '))
            contract.functions.Validator_Points(ipt_address,pt).transact()
        print("--- Scores are recorded ---")
        contract.functions.valEstim(ipt_address).transact()
        valScore = contract.functions.valEstim(ipt_address).call()
        #print(f'Validator score is: {valScore}')
    else:
        print("--- Address not correct ---")
        

def user(address):
    #print(type(address))
    ipt_address = input("Enter the User address :")
    #print(type(ipt_address))
    if ipt_address in address:
        print("\nBased on the questions award 1/0 points")
        for i in range(1,6):
            pt = int(input(f'question {i}: '))
            contract.functions.user_Points(ipt_address,pt).transact()
        print("--- Scores are recorded ---")    
        contract.functions.userEstim(ipt_address).transact()
        UserScore = contract.functions.userEstim(ipt_address).call()
        # print(f'\nUser score is: {UserScore}')
    else:
        print("\n--- Address not correct ---\n")     
    

# Main
# connection to truffle and getting 5 accounts
try:
    web3 = Web3(HTTPProvider('http://127.0.0.1:9545'))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    entity = web3.eth._get_accounts()
    user1 = entity[4]
except: 
    print("Connection error!!")
  # users in the network
    #Application Binary Interface
compiled_contract_path = 'build/contracts/ItemScore.json'

    # Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x12C483a2FC67226b6BD17206D20ab578E2281262'

with open(compiled_contract_path) as file:
   contract_json = json.load(file)  # load contract info as JSON
   contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    
    # Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

user_address = []
print("\n---- Welcome!!! What would you like to do today? ----\n")
while True:
  
    response = input(" \n 1. To add new user\n 2. User points\n 3. Validator points\n 4. To compare validator and user points\n 5. To exit\n")
    if response == '2':
        print("   --- User---   \n")
        user(user_address)
    elif response == '3':
        print("   --- Validator ---   \n")
        validator(user_address)
    elif response  == '4':
        print("   --- Comparing points--- \n")
        comparePoints(user_address)
    elif response == '1':
        print("   --- Add new User---   \n")
        user_add = newUser(entity)
        user_address.append(user_add)
        print(f'Addresses on the list: {user_address}')
    elif response == '5':
        print("---- collection completed ----\n")
        break
    else:
        print("wrong option")



