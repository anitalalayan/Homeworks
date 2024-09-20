from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional



class TransactionManager(ABC):
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...

    @abstractmethod
    def show_transaction_history(self) -> None:
        ...

class Transaction:
    def __init__(self, from_account: 'Account' , to_account: Optional['Account'], amount: float, transaction_type: str):
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount
        self._transaction_type = transaction_type
        self._timestamp = datetime.now()

    def log(self) -> None:
        print(f"Transaction Log:")
        print(f"Type: {self._transaction_type}")
        print(f"Amount: {self._amount}")
        print(f"From Account: {self._from_account._account_number}")
        if self._to_account:
            print(f"To Account: {self._to_account._account_number}")
        print(f"Timestamp: {self._timestamp}")


