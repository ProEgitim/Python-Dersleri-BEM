hak=3
while(hak):
    kullanıcıAdi=input("Kullanıcı adi giriniz:")
    sifre=input("Sifre giriniz:")

    if kullanıcıAdi== "Alper" :
        if sifre=="123":
            print("Hoşgeldiniz")


        else:
            print("Şifre Yanlış")

    else:
        print("hatalı giriş son hak",hak-1)   
        hak-=1
        a+=1

if a==3:
    print("hakkınız doldu")                 



       