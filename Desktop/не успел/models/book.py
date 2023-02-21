class Book:
    
    """Модель книги нашего проекта"""
    
    def __init__(
        self, 
        title: str,
        description: str,
        list_count: int,
        price: float, 
        rate_list:list[int]) -> None:

        self.title = title
        self.description = description
        self.price = price
        self.rate_list = rate_list
        self.list_count = list_count
    
    @property
    def rate(self):
        return round(sum(self.rate_list) / len(self.rate_list),2)

    def save() -> 'Book':
        pass
        
    def delete() -> None:
        pass
