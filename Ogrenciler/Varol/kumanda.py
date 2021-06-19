import random
import time
class Kumanda():
    def __init__(self,tvDurum="Kapalı",tvSes=0,kanalListesi=["Trt"],kanal="Trt"):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi=kanalListesi
        self.kanal=kanal
    def tvAc(self):
        if (self.tvDurum=="Açık"):
            print("TV Zaten açık...")
        else:
            print("TV açılıyor...")
            self.tvDurum="Açık"
    def tvKapat(self):
        if (self.tvDurum=="Kapalı"):
            print("TV Zaten kapalı...")
        else:
            print("TV kapanıyor...")
            self.tvDurum="Kapalı"
    def tvSesAyari(self):
        while True:
            cevap=input("Sesi Azalt: '-'\nSesi Arttır: '+'\nÇıkış: 'q'")
            if (cevap=="-"):
                if (self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses:",self.tvSes)
            elif(cevap=="+"):
                if (self.tvSes!=30):
                    self.tvSes+=1
                    print("Ses:",self.tvSes)
            elif(cevap=="q"):
                print("Ses güncellendi, çıkış yapılıyor, Ses:",self.tvSes)
                break
            else:
                print("Yanlış giriş yaptınız!")
    def kanalEkle(self,kanalAdi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanalListesi.append(kanalAdi)
        print("Kanal Eklendi.")
    def rastgeleKanal(self):
        rastgele=random.randint(0,len(self.kanalListesi)-1)
        self.kanal=self.kanalListesi[rastgele]
        print("Şuan açık olan kanal:",self.kanal)
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv Durumu: {}\nKanal Listesi: {}\nŞu anki kanal: {}\nTV Ses: {}\n".format(self.tvDurum,self.kanalListesi,self.kanal,self.tvSes)
kumanda=Kumanda()
print("""
TV Uygulaması:

1.Tv Aç
2.Tv Kapa
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı
6.Rastgele Kanal
7.Tv Bilgileri

Çıkmak için 'w' tuşuna basın.
""")
while True:
    islem=input("İşlemi Seçiniz:")
    if (islem=="w"):
        print("Program sonlanıyor...")
        time.sleep(1)
        break
    elif(islem=="1"):
        kumanda.tvAc()
    elif(islem=="2"):
        kumanda.tvKapat()
    elif(islem=="3"):
        kumanda.tvSesAyari()
    elif(islem=="4"):
        kanalAdlari=input("Kanal adlarını ',' ile ayırarak giriniz:")
        kanalListesi=kanalAdlari.split(",")
        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    elif(islem=="5"):
        print("Kanal Sayısı:",len(kumanda))
    elif(islem=="6"):
        kumanda.rastgeleKanal()
    elif(islem=="7"):
        print(kumanda)
    else:
        print("Geçersiz giriş...")