class Account:
    def __init__(self, number: str, owner: str, balance: int | float = 0):
        if balance < 0:
            raise ValueError("начальный остаток не может быть отриц.")
            
        self._number = number
        self._owner = owner 
        self._balance = balance 
        
    @property   
    def number(self) -> str:
        return self._number
        
    @property        
    def owner(self) -> str:
        return self._owner
        
    @property        
    def balance(self) -> int | float: 
        return self._balance    
    
    def deposit(self, amount: int | float):
        if amount <= 0:
            raise ValueError("сумма пополнения должна быть положительной")
        self._balance += amount
        
    def withdraw(self, amount: int | float):
        if amount <= 0:
            raise ValueError("сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("недостаточно средств на счете")
        self._balance -= amount
        
    def __repr__(self) -> str:
        return f"Account('{self._number}', '{self._owner}', {self._balance})"
        

class SavingsAccount(Account):
    def __init__(self, number: str, owner: str, balance: int | float = 0, rate: float = 0.05):
        super().__init__(number, owner, balance)
        self.rate = rate 
    
    def add_interest(self):
        interest = self._balance * self.rate 
        self._balance += interest
        
    def __repr__(self) -> str:
        return f"SavingsAccount('{self.number}', '{self.owner}', {self.balance}, {self.rate})"
        

class CheckingAccount(Account):
    def __init__(self, number: str, owner: str, balance: int | float = 0, overdraft: int | float = 0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft
        
    def withdraw(self, amount: int | float):
        if amount <= 0:
            raise ValueError("сумма снятия должна быть положительной")
        if self._balance - amount < -self.overdraft:
            raise ValueError("превышен лимит овердрафта")
        self._balance -= amount
    
    def __repr__(self) -> str:
        return f"CheckingAccount('{self.number}', '{self.owner}', {self.balance}, {self.overdraft})"


s = SavingsAccount("1", "Иван", 1000, rate=0.1)
s.add_interest()
print(s.balance)

try:
    s.withdraw(2000)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    s.balance = 0
except AttributeError as e:
    print(f"Ошибка: {e}")

c = CheckingAccount("2", "Мария", 100, overdraft=500)
c.withdraw(400)
print(c.balance)

try:
    c.withdraw(300)
except ValueError as e:
    print(f"Ошибка: {e}")

c.deposit(1000)
print(c.balance)
print(isinstance(c, Account))