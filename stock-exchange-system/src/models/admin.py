from src.models.account import Account
from src.choices.account_status import AccountStatus


class Admin(Account):
    """Admin model class."""

    def block_account(self, account):
        """Block user account."""
        account.status = AccountStatus.BLOCKED

    def unblock_account(self, account):
        """Unblock user account."""
        account.status = AccountStatus.ACTIVE
