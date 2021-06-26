import random
import time
class Kumanda():
    def __init__(self, tvDurum="Kapalı", tvSes=0,kanalListesi=["Trt"], kanal="Trt"):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi=kanalListesi
        self.kanal=kanal

    def tvAc(self):
        if(self.tvDurum=="Açık"):
            print("Tv Zaten Açık")
        else:
            print("Tv Açılıyor...")
            self.tvDurum="Açık"
    def tvKapat(self):
        if(self.tvDurum=="Kapalı"):
            print("Tv Zaten Kapalı")
        else:
            print("Tv Kapalı...")
            self.tvDurum="Kapalı"

    def tvSesayari(self):
        while True:
            cevap=input("Sesi Azalt: '-'\nSesi Arttır:  '+'\nÇıkış: 'q'")
            if (cevap=="-"):
                if(self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses:",self.tvSes)
            elif(cevap=="+"):
                if (self.tvSes!)

            print("Tv Zaten Kapalı")
        else:
            print("Tv Kapalı...")
            self.tvDurum="Kapalı"