from web3 import Web3
from src.wallet_parser import evm_wallets, evm_readable_wallets

web3 = Web3(Web3.HTTPProvider(r'https://testnet-rpc.monad.xyz/'))

def monad_check(evm_wallets):
    balances = []
    
    for wallet, readable_wallet in zip(evm_wallets, evm_readable_wallets):
        wei_balance = web3.eth.get_balance(wallet)
        mon_balance = web3.from_wei(wei_balance, 'ether')
        
        balances.append(str(readable_wallet) + ": " + str(mon_balance) + ' MON')
    
    return balances
