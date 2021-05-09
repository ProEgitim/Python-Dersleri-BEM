kullanici=input("kullanici adi giriniz ")
sifre=input("sifre giriniz ")

if kullanici == "Erdogan":
    if sifre == "123":
        print("Hoşgeldiniz..")
    else:
        print("Şifre yanlış")
else:
    print("hatalı giriş")
    