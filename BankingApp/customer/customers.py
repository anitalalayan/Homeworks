from typing import List
from accounts.account import Account

class Customer:
    def __init__(self, name: str, contact_info: str):
        self._name = name
        self._contact_info = contact_info
        self._accounts: List[Account] =  []

    def add_account(self, account: Account) -> None:
        self._accounts.append(account)
        print(f"Added account {account._account_number} for customer {self._name}")

    def view_accounts(self) -> None:
        print(f"Accounts for customer {self._name}:")
        for account in self._accounts:
            print(
                f"Account Number: {account._account_number}, Type: {account.get_account_type()}, Balance: {account._balance}")

    def view_transaction_history(self) -> None:
        print(f"Transaction History for customer {self._name}:")
        for account in self._accounts:
            account.show_transaction_history()
