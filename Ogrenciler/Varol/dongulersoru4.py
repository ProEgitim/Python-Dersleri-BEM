toplam=0
while True:
    sayi=input("Bir sayı giriniz:")
    if (sayi=="q"):
        break
    toplam+=int(sayi)
print("Girdiğiniz sayıların toplamı:",toplam)
