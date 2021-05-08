print("""

-------------KULLANICI GİRİŞ EKRANI----------

""")

Kullaciadi_ID = "Kullanici"
Kullaciadi_PW= "123"

kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifre'yi Giriniz: ")

if (kullanici_adi == Kullaciadi_ID) and (sifre != Kullaciadi_PW):
    print("Dikkat Şifre Yanlış..!!")

elif (kullanici_adi != Kullaciadi_ID) and (sifre == Kullaciadi_PW):
    print("Dikkat Kullanıcı Adı Yanlış..")

elif (kullanici_adi != Kullaciadi_ID) and (sifre != Kullaciadi_PW):
    print("Dikkat Kullanıcı Adı Ve Şifre yanlış..")
else:
    print("Giriş yapıldı!")