class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def show_info(self):
        print(f"The title: {self.title}, the director: {self.director}, movie time: {self.duration} minutes")

    def is_long(self):
        if self.duration > 120:
            return True
        else:
            return False

    def add_minutes(self, n):
        self.duration += n

p1 = Movie("The Eras Tour", "Sam Wrench", 169)
p1.show_info()
print(p1.is_long())
p1.add_minutes(50)
p1.show_info()
