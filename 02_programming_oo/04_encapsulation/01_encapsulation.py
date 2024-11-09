class Account:
    def __init__(self, nro_agency, balance=0):
        self._balance = balance
        self.nro_agency = nro_agency

    def deposity(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

account = Account("0001", 100)
account.deposity(500)
print(account.nro_agency)
print(account.get_balance())
