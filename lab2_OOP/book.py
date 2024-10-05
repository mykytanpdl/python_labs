class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f'book "{self.title}" by {self.author}'