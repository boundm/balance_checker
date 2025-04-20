from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.eth_checker import eth_check
from src.monad_checker import monad_check
from src.solana_checker import solana_check

from src.wallet_parser import evm_wallets, solana_wallets
console = Console()

def show_menu():
    console.print(Panel.fit("💰 [bold cyan]Crypto Wallet Checker[/bold cyan]", border_style="green"))
    
    console.print(f"Загружено {len(evm_wallets)} кошельков evm")
    console.print(f"Загружено {len(solana_wallets)} кошельков solana\n")

    console.print("[1] Ethereum")
    console.print("[2] Monad")
    console.print("[3] Solana")
    console.print("[4] Exit")

    choice = Prompt.ask("\n[bold yellow]Выбери блокчейн для проверки[/bold yellow]", choices=["1", "2", "3", "4"])
    return choice

def main():
    choice = show_menu()
    if choice == "1":
        console.print("[bold green]Чекаю Ethereum\n")
        eth_check()
    
    elif choice == "2":
        console.print("[bold green]Чекаю Monad\n")
        monad_balances = monad_check(evm_wallets)
        
        for counter, monad_balance in enumerate(monad_balances, start=1):
            console.print(f'[bold green]{counter:>2}.[bold white] {monad_balance}')
    
    elif choice == "3":
        console.print("[bold green]Чекаю Solana[/bold green]\n")
    
    else:
        console.print("[red]Неверный выбор. Выход.[/red]\n")
        exit()


if __name__ == "__main__":
    main()