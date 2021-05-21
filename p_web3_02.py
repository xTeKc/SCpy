

import os
from dotenv import load_dotenv

from web3 import Web3

load_dotenv()
node_provider2 = os.environ['NODE_PROVIDER'] 
web3_connection2 = Web3(Web3.HTTPProvider(node_provider))


contract_address2 = config('CONTRACT_ADDRESS')

contract_abi2 = config('CONTRACT_ABI')



def is_connected2():
	print(web3_connection.isConnected())