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
            

class Reader:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.pages_read = 0 


class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, book: Book):
        self._books.append(book)
        
    def find_by_isbn(self, isbn: str) -> Book | None:
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
        
    def find_by_author(self, author: str) -> list[Book]:
        return [book for book in self._books if book.author == author]
        
    def lend(self, isbn: str, reader: Reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError(f"книга с isbn {isbn} отсутствует в библиотеке")
            
        book.borrow()
        reader.books.append(book)
        
    def take_back(self, isbn: str, reader: Reader, pages_read: int):
        book_to_return = None
        for book in reader.books:
            if book.isbn == isbn:
                book_to_return = book
                break
            
        if book_to_return is None:
            raise ValueError(f"у читателя {reader.name} нет книги с isbn {isbn}")
            
        book_to_return.give_back(pages_read)
        reader.books.remove(book_to_return)
        reader.pages_read += pages_read
        
    def available(self) -> list[Book]:
        return [book for book in self._books if book.is_available]
        
    def unfinished(self) -> list[Book]:
        return [
            book for book in self._books
            if 0 < book.last_read_pages < book.pages
        ]
        
    def __len__(self) -> int:
        return len(self._books)


lib = Library()
lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
alice = Reader("Алиса")

lib.lend("123", alice)
print(alice.books)
print(lib.find_by_isbn("123").is_available)
print(len(lib.available()))

try:
    lib.lend("123", Reader("Боб"))
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    lib.take_back("123", alice, 500)
except ValueError as e:
    print(f"Ошибка: {e}")

print(alice.books)
lib.take_back("123", alice, 100)
print(alice.books)
print(alice.pages_read)
print(lib.unfinished())

lib.lend("124", alice)
lib.take_back("124", alice, 112)
print(alice.pages_read)
print(len(lib.unfinished()))