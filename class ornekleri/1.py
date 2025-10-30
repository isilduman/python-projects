#sınıf isimleri büyük harf ile başlar
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Merhaba, ben {self.name}, {self.age} yaşındayım!")

    def change_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'in yeni yaşı: {self.age}")

    def is_adult(self):
        return self.age >= 18

# Nesne oluştur
p1 = Person("İsıl", 17)

p1.greet()              # bilgiyi göster
p1.change_age(19)       # yaşı değiştir
print(p1.is_adult())    # True veya False döner

