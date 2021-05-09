while(True):
    sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
    deger = 1
    for i in range(sayi):
        deger = deger * (i+1)
    
    print("Faktoriyel : ", deger)