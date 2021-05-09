hak=3
while(hak):
    kullanici=input("kullanici adi giriniz ")
    sifre=input("sifre giriniz ")
    
    if kullanici == "Erdogan":
        if sifre == "123":
            print("Hoşgeldiniz..")
            hak = 0
        else:
            print("Şifre yanlış")
    else:
        print("hatalı giriş son hak",hak-1)
        hak-=1
print("hakkınız doldu")