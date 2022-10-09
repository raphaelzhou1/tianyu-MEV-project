from etherscan import Etherscan
# from enums import Actions as actions

# Methods: https://github.com/pcko1/etherscan-python/tree/master/logs/standard

# print(ActionsEnum.Balances)

ether_api_key = 'TE9HIXVD4MTIGAP9SJB8F3V4E39UTP8C1E'
eth = Etherscan(ether_api_key)

print("Hello")

Wallet_Addresses = ["0xc3d688B66703497DAA19211EEdff47f25384cdc3", "0x42F9505a376761b180e27a01bA0554244ED1DE7D"]
eth_balances = eth.get_eth_balance_multiple(Wallet_Addresses)
print(eth_balances)
