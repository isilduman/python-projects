F=float(input("Enter temperature in Fahrenheit: "))
def fahrenheit_celsius(F):
    C=(F-32)*5/9
    return C
result=fahrenheit_celsius(F)
print(f"{F} Fahrenheit is {result:.2f} Celsius") #ondalık basamak sayısını ayarlamak için sayı.f kullanılır
