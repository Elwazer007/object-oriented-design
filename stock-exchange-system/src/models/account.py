from abc import ABC

from src.choices.account_status import AccountStatus


class Account(ABC):
    """Account model class."""

    def __init__(
        self,
        id: int,
        status: AccountStatus,
        email: str,
        password: str,
        phone: str,
        address,
    ):
        self.id = id
        self.status = status
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address

    def reset_password(self, new_password):
        """Reset account password."""
        self.password = new_password
