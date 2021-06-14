def mukemmel(sayi):
    mukemmel_sayilar = []
    for i in range(1, sayi):
        toplam = 0
        for j in range(1, i):
           if i % j == 0:
               toplam += j
        if toplam == i:
           mukemmel_sayilar.append(i)
    return mukemmel_sayilar
           
           
print(mukemmel(1000))


