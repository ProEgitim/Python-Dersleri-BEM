print("-------Kullanıcı Girişi------")

kullaniciAdi = "Ersan"
Sifre = "37726"

a = input("Lütfen Kullanıcı Adınızı Giriniz: ")
b = input("Lütfen Şİfre Giriniz: ")
if (a.lower() != kullaniciAdi.lower()):
    print("Kullanıcı adı doğru değil")
elif (b != Sifre):
    print("Şifreniz Doğru Değil")
elif (a.lower() != kullaniciAdi.lower()) and (b != Sifre):
    print("Kullanıcı Adı ve Şifreniz Yanlış")
else:
    print('Kullanıcı Adı ve Şİfre Doğru. Sisteme Hoşgeldiniz.')

