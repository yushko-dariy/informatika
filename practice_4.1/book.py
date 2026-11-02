class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int, pages: int):
        if pages <= 0:
            raise ValueError("кол-во стр должно быть положительным")
            
        self._title = title
        self._author = author 
        self._isbn = isbn 
        self._year = year
        self._pages = pages
        
        self._is_available = True
        self._last_read_pages = 0 
        
    @property
    def title(self) -> str:
        return self._title
        
    @property    
    def author(self) -> str:
        return self._author
        
    @property    
    def isbn(self) -> str:
        return self._isbn
        
    @property    
    def year(self) -> int:
        return self._year
        
    @property    
    def pages(self) -> int:
        return self._pages
        
    @property    
    def is_available(self) -> bool:
        return self._is_available
        
    @property   
    def last_read_pages(self) -> int:
        return self._last_read_pages
        
    def borrow(self):
        if not self._is_available:
            raise ValueError("книга уже выдана")
        self._is_available = False
            
    def give_back(self, pages_read: int):
        if self._is_available:
            raise ValueError("книга уже на полке")
        if not (0 <= pages_read <= self._pages):
            raise ValueError(f"в книге всего {self._pages} страниц")
            
        self._last_read_pages = pages_read
        self._is_available = True 
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._isbn == other._isbn
            
    def __lt__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._year < other._year
        
    def __repr__(self) -> str:
        return f"Book('{self._title}', '{self._author}', '{self._isbn}', {self._year}, {self._pages})"

b = Book("1984", "Оруэлл", "123", 1949, 328)
print(b.is_available)
print(b.last_read_pages)
b.borrow()
print(b.is_available)

try:
    b.borrow()
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    b.is_available = True
except AttributeError as e:
    print(f"Ошибка: {e}")

try:
    b.give_back(400)
except ValueError as e:
    print(f"Ошибка: {e}")

print(b.is_available)
b.give_back(120)
print(b.last_read_pages)
print(b == Book("1984", "Оруэлл", "123", 1949, 328))

old = Book("Мы", "Замятин", "456", 1924, 224)
print(sorted([b, old]))