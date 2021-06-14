class Yazilimci():
    def __init__(self,isim,soyisim,sicil,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.sicil=sicil
        self.maas=maas
        self.diller=diller
    def bilgileriGoster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim: {}
        
        Soyisim: {}
        
        Sicil No: {}
        
        Maaş: {}
        
        Bilgiği Diller: {}
        """.format(self.isim,self.soyisim,self.sicil,self.maas,self.diller))
    def dilEkle(self,yenidil):
        print ("dil ekleniyor...")
        self.diller.append(yenidil)
    def maasZammi(self,zam):
        print("Maaşa Zam Yapılıyor...")
        self.maas+=zam
yazilimci1=Yazilimci ("Ali", "Aktaş",123456, 15000,["Python","C"])
yazilimci1.dilEkle("Go")
yazilimci1.maasZammi(500)
yazilimci1.bilgileriGoster()
