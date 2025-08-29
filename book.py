class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.__price = price  

    def display_info(self):
        return f"'{self.title}' by {self.author} ({self.year}) - ${self.__price:.2f}"

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def category(self):
        return "General Book"

class Fiction(Book):
    def __init__(self, title, author, year, price, genre):
        super().__init__(title, author, year, price)
        self.genre = genre

    def category(self): 
        return f"Fiction - Genre: {self.genre}"

class Textbook(Book):
    def __init__(self, title, author, year, price, subject):
        super().__init__(title, author, year, price)
        self.subject = subject

    def category(self): 
        return f"Textbook - Subject: {self.subject}"
