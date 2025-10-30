class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"{self.name}'s grade: {self.grade}")

    def is_passed(self):
        if self.grade >= 60:
            return True
        else:
            return False

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s new grade: {self.grade}")

p1 = Student("isil", 95)
p1.show()
print(p1.is_passed())  # ← buraya print ekledik
p1.update_grade(92)
p1.show()
