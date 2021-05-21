

import os
from dotenv import load_dotenv

from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER'] 
web3_connection = Web3(Web3.HTTPProvider(node_provider))


contract_address = config('CONTRACT_ADDRESS')

contract_abi = config('CONTRACT_ABI')