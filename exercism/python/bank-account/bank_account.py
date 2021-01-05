from threading import Lock

class BankAccount:
    def __init__(self):
        self.lock = Lock()
        self.opened = False
        self.balance = 0

    def get_balance(self):
        if(self.opened == True):
            return self.balance
        else:
            raise(ValueError("can't get balance on closed account"))

    def open(self):
        if(self.opened == False):
            self.opened = True
            self.balance = 0
        else:
            raise(ValueError("already open"))

    def deposit(self, amount):
        if(self.opened and amount >= 0):
            with self.lock:
                self.balance = self.balance + amount
        else:
            raise(ValueError("bad deposit"))

    def withdraw(self, amount):
        if(self.opened and self.balance >= amount and amount > 0):
            with self.lock:
                self.balance = self.balance - amount
        else:
            raise(ValueError("bad withdraw"))

    def close(self):
        if(self.opened == True):
            self.opened = False
        else:
            raise(ValueError("account already closed"))