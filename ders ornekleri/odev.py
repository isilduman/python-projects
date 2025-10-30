def en_buyuk_sayi(liste):
    en_buyuk=liste[0]
    for sayi in liste:
        if sayi>en_buyuk:
            en_buyuk=sayi
    return en_buyuk
sayi=[12,65,89,87,4,81,44,16]
print("listedeki en büyük sayi: ",en_buyuk_sayi(sayi))