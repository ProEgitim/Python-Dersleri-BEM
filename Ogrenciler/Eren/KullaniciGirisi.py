# print("""

# -------------KULLANICI GİRİŞ EKRANI----------

# """)

# Kullaciadi_ID = "Kullanici"
# Kullaciadi_PW= "123"

# kullanici_adi = input("Kullanıcı Adını Giriniz: ")
# sifre = input("Şifre'yi Giriniz: ")

# if (kullanici_adi == Kullaciadi_ID) and (sifre != Kullaciadi_PW):
#     print("Dikkat Şifre Yanlış..!!")

# elif (kullanici_adi != Kullaciadi_ID) and (sifre == Kullaciadi_PW):
#     print("Dikkat Kullanıcı Adı Yanlış..")

# elif (kullanici_adi != Kullaciadi_ID) and (sifre != Kullaciadi_PW):
#     print("Dikkat Kullanıcı Adı Ve Şifre yanlış..")
# else:
#     print("Giriş yapıldı!")



kullanici_adim="Kullanici"
 
parolam ="123"
 
giris_hakki=3
 
while giris_hakki>0:
    giris_hakki -=1
    kullanici_adi = input("Kullanıcı Adınızı Girin :")
 
    parola = input("Parolayı Giriniz :")
 
    if kullanici_adi==kullanici_adim and parola== parolam:
 
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
        giris_hakki=0
        print("Hoşgeldiniz..")
    elif (kullanici_adi == kullanici_adim) and (parola != parolam):
        print("Dikkat Şifre Yanlış..!! Son ",giris_hakki,"Hakkınız kaldı.")
        
    elif (kullanici_adi != kullanici_adim) and (parola == parolam):
        print("Dikkat Kullanıcı Adı Yanlış..Son ",giris_hakki,"Hakkınız kaldı.")
        
    elif (kullanici_adi != kullanici_adim) and (parola != parolam):
        print("Dikkat Kullanıcı Adı Ve Şifre yanlış..Son ",giris_hakki,"Hakkınız kaldı.")

    else:
 
        print("Kullanıcı bilgileri yanlış tekrar deneyin! Son Hakkınız",giris_hakki)