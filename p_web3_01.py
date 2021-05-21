
from web3 import Web3
from decouple import config


node_provider = config('NODE_PROVIDER')

web3_connection = Web3(Web3.HTTPProvider(node_provider))

def is_connected():
	print(web3_connection.isConnected())
