class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"the book name: {self.title}, the author: {self.author}, book page: {self.pages}")

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False

    def add_pages(self, n):
        self.pages += n

p1 = Book("Fourth Wing", "Rebecca Yarros", 656)
p1.show_info()
print(p1.is_long())  # True
p1.add_pages(50)
p1.show_info()       # 706 sayfa olur
