evm_wallets = []
solana_wallets = []
evm_readable_wallets = []
solana_readable_wallets = []

with open('wallets.txt', 'r') as wallets:
    for wallet in wallets:
        if wallet.startswith('0x'):
            evm_wallets.append(wallet[:-1])
        else: solana_wallets.append(wallet)
    
    evm_readable_wallets = [w[:4] + '...' + w[-4:] for w in evm_wallets]
    solana_readable_wallets = [w[:4] + '...' + w[-4:] for w in solana_wallets]


