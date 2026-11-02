from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, weight: int | float):
        self.name = name
        self.weight = weight
        
    @abstractmethod
    def sound(self) -> str:
        """возвращает звук, которое издает животное"""
        pass
    
    @abstractmethod
    def food_per_day(self) -> int | float:
        """возвращает кол-в корма в килограммах в день"""
        pass
    
    def describe(self) -> str:
        """возвращает базовое описание животного"""
        return f"{self.name}: {self.sound()}"
        

class Lion(Animal):
    def sound(self) -> str:
        return "Р-р-р"
        
    def food_per_day(self) -> int | float:
        return self.weight * 0.05
        

class Parrot(Animal):
    def sound(self) -> str:
        return "Привет!"
        
    def food_per_day(self) -> int | float:
        return self.weight * 0.10


class Zoo:
    def __init__(self):
        self._animals = []
        
    def add(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError("в зоопарк можно добавить объект только класса Animal")
        self._animals.append(animal)
        
    def sounds(self) -> list[str]:
        return [animal.describe() for animal in self._animals]
        
    def total_food(self) -> int | float:
        return sum(animal.food_per_day() for animal in self._animals)
    
    def __len__(self) -> int:
        return len(self._animals)


zoo = Zoo()
zoo.add(Lion("Симба", 190))
zoo.add(Parrot("Кеша", 0.5))

print(len(zoo))
print(zoo.sounds())
print(zoo.total_food())

try:
    Animal("Нечто", 10)
except TypeError as e:
    print(f"Ошибка создания абстрактного класса: {e}")

try:
    zoo.add("слон")
except TypeError as e:
    print(f"Ошибка добавления в зоопарк: {e}")