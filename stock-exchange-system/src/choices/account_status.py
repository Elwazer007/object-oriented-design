from enum import Enum


class AccountStatus(Enum):
    """Account status choices."""

    ACTIVE = 1
    DEACTIVATED = 2
    DELETED = 3
    NONE = 4
    BLOCKED = 5
