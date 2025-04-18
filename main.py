from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.eth_checker import eth_check

console = Console()

def show_menu():
    console.print(Panel.fit("💰 [bold cyan]Crypto Wallet Checker[/bold cyan]", border_style="green"))
    console.print("[1] Ethereum")
    console.print("[2] Monad")
    console.print("[3] Solana")
    console.print("[4] Exit")

    choice = Prompt.ask("\n[bold yellow]Выбери блокчейн для проверки[/bold yellow]", choices=["1", "2", "3", "4"])
    return choice

def main():
    choice = show_menu()
    if choice == "1":
        console.print("[bold green]Чекаю Ethereum")
        eth_check()
    
    elif choice == "2":
        console.print("[bold green]Чекаю Monad")
    
    elif choice == "3":
        console.print("[bold green]Чекаю Solana[/bold green]")
    
    else:
        console.print("[red]Неверный выбор. Выход.[/red]")
        exit()


if __name__ == "__main__":
    main()