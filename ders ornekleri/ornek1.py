#dışardan parametre almayan fonksiyon
def ortalama1():
    a=30
    b=40
    c=60
    ortalama=(a+b+c)/3
    print("ortalama: ",ortalama)
ortalama1()
#dışardan parametre alan fonksiyon
def ortalama2(a,b,c):
    ort=(a+b+c)/3
    print("ortalama: ", ort)
ortalama2(30,40,60)
#dışardan parametre almayan değer döndüren fonksiyon
def ortalama3():
    a=30
    b=40
    c=60
    return (a+b+c)/3
print("ortalama: ",ortalama3())
#dışardan parametre alan değer döndüren fonksiyon
def ortalama4(a,b,c):
    return (a+b+c)/3
sonuc=ortalama4(30,40,60)
print("ortalama: ",sonuc)
#dışardan varsayılan parametre alan ve geriye değer döndüren fonksiyon tanımlaması
def ortalama5(a=30,b=40,c=60):
    return (a+b+c)/3
    return ort
print("varsayılan ortalama: ",ortalama5())
print("yeni ortalama: ",ortalama5(20,30,50))