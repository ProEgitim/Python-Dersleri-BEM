class Calisan():
    def __init__(self,isim,maas):
        print("Çalışan sınıfının init fonksiyonu çalıştı")
        self.isim=isim
        self.maas=maas
class Yonetici(Calisan):
    def __init__(self,isim,maas,kisiSayisi):
        super().__init__(isim,maas)
        # def __init__(self,isim,maas):
        # print("Çalışan sınıfının init fonksiyonu çalıştı")
        # self.isim=isim
        # self.maas=maas
        print("Yönetici sınıfının init fonksiyonu çalıştı")
        self.kisiSayısı=kisiSayisi
# calisan1=Calisan("Varol",5000)
yonetici1=Yonetici("Deniz",4000,20)

print(yonetici1.isim,yonetici1.maas,yonetici1.kisiSayısı)