print("-------Kullanıcı Girişi---------")

kullaniciAdi="Ekrem"
parola="369258"

username=input("Kullanıcı Adınızı Giriniz")
password=input("Parolanızı Giriniz")

if username==kullaniciAdi and password==parola:
    print("Tebrikler başarılı giriş yaptınız.")

elif username!=kullaniciAdi and password==parola:
    print("kullanıcı adını yanlış girdiniz.")
elif username==kullaniciAdi and password!=parola:
    print("Şifreyi yanlış girdiniz.")
elif username==kullaniciAdi and password!=parola:
    print("Kullanıcı ve Şifreyi yanlış Girdiniz.")