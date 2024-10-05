from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.status = 'active'

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()