print("""Sayı Tahmin Oyunu
--------------------------
""")
sayi = 17

while True:
    tahmin=int(input("LÜtfen bir sayı giriniz:"))
    if (tahmin == sayi):
        print("Tebrikler doğru tahmin yine bekleriz")
        break
    elif(tahmin != sayi):
        print("Lütfen tahmininizi yenileyin")
    
    
    