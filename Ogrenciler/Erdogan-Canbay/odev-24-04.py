"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın
kullanıcdan ad soyad numara alıp alt alta yazdır
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
"""

def soru1():
    print("_____________________Soru1_____toplam ödeme hesaplama__________________________")
    fiyat=float(input("yakıt ücreti (km/tl) = "))
    print("Toplam alınan yol kaç km ?")
    yol=float(input("yol (km)= "))
    sonuc=fiyat*yol
    print("toplam yolunuz {} km \nToplam borcunuz {}₺".format(yol,sonuc))
    return "Soru1 islem sonu\n"

def soru2():
    print("______________________Soru2______ad soyad numara alıp alt alta yazdırma_______________")
    Ad=str(input("Adınız= "))
    Soyad=str(input("Soyad= "))
    Numara=str(input("Numara= "))
    print("Ad:{}\nSoyad:{}\nNumara:{}".format(Ad,Soyad,Numara))
    return "Soru2 islem sonu\n"

def soru3():
    print("______________________Soru3___Hipotenüs Hesaplama____________________________")
    kenar1=int(input("birinci kenarı girin= "))
    kenar2=int(input("ikinci kenarı girin= "))
    kareToplam= (kenar1*kenar1) + (kenar2*kenar2)
    print("Hesaplanan hipotenüs değeri= ",kareToplam ** 0.5)
    kok:float=1.0

    for sayac in range(1,kareToplam) :
        kok = (kareToplam/kok+kok)/2
    print("Yaklaşık hipotenüs değeri= ",kok)
    return "Soru3 islem sonu\n"

while True:
    secim=int(input("Cözmek istediğiniz soruyu belirtiniz..(1-2-3) Cikmak icin 0 giriniz "))
    if secim == 0:
        print("Cikis yapıldı")
        break
    operations=[soru1,soru2,soru3]
    cikti = operations[secim-1]()
    print(cikti)
    

    

