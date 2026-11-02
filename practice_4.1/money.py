from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, rubles, kopecks=0):
        if not isinstance(rubles, int) or not isinstance(kopecks, int):
            raise TypeError()
            
        total_kopecks = rubles * 100 + kopecks
        
        if total_kopecks < 0:
            raise ValueError()
            
        self._rubles = total_kopecks // 100
        self._kopecks = total_kopecks % 100

    @property
    def rubles(self):
        return self._rubles

    @property
    def kopecks(self):
        return self._kopecks

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.rubles + other.rubles, self.kopecks + other.kopecks)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.rubles - other.rubles, self.kopecks - other.kopecks)
        return NotImplemented

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError()
        if other < 0:
            raise ValueError()
            
        total_kopecks = (self.rubles * 100 + self.kopecks) * other
        return Money(0, total_kopecks)

    def __rmul__(self, other):
        return self.__mul__(other)

    def split(self, n):
        if not isinstance(n, int) or n < 1:
            raise ValueError()
            
        total_kopecks = self.rubles * 100 + self.kopecks
        base_part = total_kopecks // n
        remainder = total_kopecks % n
        
        result = []
        for i in range(n):
            current_kopecks = base_part + (1 if i < remainder else 0)
            result.append(Money(0, current_kopecks))
            
        return result

    def __eq__(self, other):
        if isinstance(other, Money):
            return (self.rubles, self.kopecks) == (other.rubles, other.kopecks)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)
        return NotImplemented

    def __repr__(self):
        return f"Money({self.rubles}, {self.kopecks})"

    def __str__(self):
        return f"{self.rubles} руб. {self.kopecks:02d} коп."


a = Money(10, 50)
b = Money(2, 75)

print(a + b)
print(a - b)

try:
    print(b - a)
except ValueError as e:
    print("Ошибка: отрицательный баланс (ValueError)")

print(a * 3)
print(3 * a)
print(sum([a, b, Money(0, 75)]))
print(Money(10).split(3))
print(Money(1, 150))
print(str(Money(5, 7)))
print(Money(1, 0) == Money(0, 100))
print(sorted([a, b]))
