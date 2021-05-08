print("-------Kullanıcı Girişi------")

kullaniciAdi = "Ersan"
Sifre = 37726

a = str(input("Lütfen Kullanıcı Adınızı Giriniz: "))
b = int(input("Lütfen Şİfre Giriniz: "))
if (a != kullaniciAdi):
    print("Kullanıcı adı doğru değil")
elif (b != Sifre):
    print("Şİfreniz Doğru Değil")
elif (a != kullaniciAdi) and (b != Sifre):
    print("Kullanıcı Adı ve Şifreniz Yanlış")
else:
    print('Kullanıcı Adı ve Şİfre Doğru. Sisteme Hoşgeldiniz.')