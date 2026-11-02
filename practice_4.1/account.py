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

acc = Account("40817", "Иван", 1000)
acc.deposit(500)
print(acc.balance)
acc.withdraw(200)
print(acc.balance)
print(acc.balance)
print(acc)
try:
    acc.withdraw(5000)
except ValueError as e:
    print(f"Ошибка: {e}")

print(acc.balance)