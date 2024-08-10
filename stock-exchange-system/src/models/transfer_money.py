from abc import ABC, abstractmethod


class TransferMoney(ABC):
    def __init__(self, amount, from_account, to_account):
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account

    @abstractmethod
    def transfer(self):
        pass


class WireTransfer(TransferMoney):
    def transfer(self):
        print(
            f"Wire transfer from {self.from_account} to {self.to_account} of {self.amount}"
        )


class ElectronicTransfer(TransferMoney):
    def transfer(self):
        print(
            f"Electronic transfer from {self.from_account} to {self.to_account} of {self.amount}"
        )
