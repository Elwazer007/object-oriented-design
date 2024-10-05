from src.models.account import Account


class Admin(Account):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def __str__(self):
        return self.name
    
    def block_user(self, user):
        pass

    def unblock_user(self, user):
        pass
