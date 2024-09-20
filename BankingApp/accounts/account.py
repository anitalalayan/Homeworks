from typing import List
from abc import ABC, abstractmethod
from transfers.transfer import Transaction, TransactionManager


class Account(TransactionManager):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type
        self._transactions: List[Transaction] = []

    @abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        ...

    @abstractmethod
    def show_balance(self) -> None:
        ...

    @abstractmethod
    def get_account_type(self) -> str:
        ...

    def  log_transaction(self, transaction_type: str, amount: float) -> None:
        transaction = Transaction(self, None, amount, transaction_type)
        self._transactions.append(transaction)
        transaction.log()


    def show_transaction_history(self) -> None:
        for transaction in self._transactions:
            transaction.log()


class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, overdraft_limit: float):
        super().__init__(account_number, balance, "Checking")
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            self.log_transaction("Deposit", amount)
        else:
            raise ValueError("Deposit amount can't be negative")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            self.log_transaction("Withdraw", amount)
        else:
            raise ValueError("Insufficient funds. Amount {amount} is greater than the current balance.")

    def transfer(self, destination: Account, amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction("Transfer", amount)

    def show_balance(self) -> None:
        print(f"CheckingAccount Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type



class SavingsAccount(Account):

    def __init__(self, account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, "Savings")
        self._interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            self.log_transaction("Deposit", amount)

        else:
            raise ValueError("Deposit amount can't be negative")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.log_transaction("Withdraw", amount)
        else:
            raise ValueError("Insufficient funds. Amount {amount} is greater than the current balance.")

    def transfer(self, destination: 'Account', amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction("Transfer", amount)

    def show_balance(self) -> None:
        print(f"Savings Account Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type



class JointAccount(Account):

    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self._joint_owners = joint_owners

    def add_owner(self, customer_name: str) -> None:
        self._joint_owners.append(customer_name)
        print(f" New owner added: {customer_name}")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            self.log_transaction("Deposit", amount)
        else:
            raise ValueError("Deposit amount can't be negative")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.log_transaction("Withdraw", amount)
        else:
            raise ValueError("Insufficient funds. Amount {amount} is greater than the current balance.")

    def transfer(self, destination: 'Account', amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction("Transfer", amount)

    def show_balance(self) -> None:
        print(f"Joint Account Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type
