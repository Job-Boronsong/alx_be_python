

class BankAccount:
    """
    Represents a bank account, managing its balance and operations.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account.
                                     Defaults to 0.0.
        """
        # Encapsulation: The balance is stored within the object.
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        # In a real scenario, you'd validate if amount > 0, but we follow the prompt's simple requirement.
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the transaction was successful, False otherwise.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Using :.2f ensures the output is formatted as currency (two decimal places).
        print(f"Current Balance: ${self.account_balance:.2f}")