import sys
from bank_account import BankAccount

def main():
    # IMPORTANT: Each time you run this script from the command line,
    # it starts fresh with a balance of 100.
    # The balance does not persist between different command executions.
    account = BankAccount(100)  # Example starting balance

    # Check for sufficient command line arguments
    if len(sys.argv) < 2:
        # Note: The prompt's example says "python main.py", we use "python main-0.py"
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the argument (sys.argv[1] is the first argument after the script name)
    # Example: If the input is "deposit:50",
    # command will be "deposit", params will be ["50"]
    command, *params = sys.argv[1].split(':')
    
    # Convert the parameter to a float if it exists, otherwise set amount to None
    amount = float(params[0]) if params else None

    # Process the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        # Check the return value of the withdraw method
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        # The display_balance method handles the printing itself
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()