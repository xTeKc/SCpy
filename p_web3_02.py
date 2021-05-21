

import os
from dotenv import load_dotenv

from web3 import Web3


contract_address = config('CONTRACT_ADDRESS')

contract_abi = config('CONTRACT_ABI')