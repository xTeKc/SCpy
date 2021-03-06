

import os
from dotenv import load_dotenv
from decouple import config
import json
from web3 import Web3

load_dotenv()
node_provider2 = os.environ['NODE_PROVIDER'] 
web3_connection2 = Web3(Web3.HTTPProvider(node_provider2))


contract_address2 = config('CONTRACT_ADDRESS')

contract_abi2 = config('CONTRACT_ABI')



def is_connected2():
	print(web3_connection2.isConnected())


def supply_ERC20():
	contract = web3_connection2.eth.contract(address=contract_address2, abi=contract_abi2)
	supply_token = web3_connection.fromWei(contract.functions.totalSupply().call(), 'ether')
	print(supply_token)


def balance_ERC20(ERC20_address):
	ERC20_address = Web3.toChecksumAddress(ERC20_address)
	contract = web3_connection2.eth.contract(address=contract_address2, abi=contract_abi2)
	balance_token = web3_connection.fromWei(contract.functions.balanceOf(ERC20_address).call(), 'ether')
	print(balance_token)