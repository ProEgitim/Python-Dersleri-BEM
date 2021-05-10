while True:
    sayi=input("LÜtfen Bir Sayı Giriniz. (Çıkmak için 'q' ya basın.) : ")

    if sayi.lower()=="q":
        print("Oyundan çıktınız. Yine bekleriz.")
        break
    
    uzunluk=len(sayi)

    toplam=0
    for i in range(uzunluk):
        toplam = toplam + int(sayi[i])**uzunluk
    
    if(toplam==int(sayi)):
        print("Girdiğiniz Sayı Bir Armstrong Sayıdır!")
    else:
        print("Girdiğiniz Sayı Armstrong Bir Sayı Değildir!")