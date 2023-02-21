from book import Book

class Store:
    def __init__(self, adress: str, book: list[Book]) -> None:
        self.adress = adress
        self.book = book