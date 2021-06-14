print("-----------Kullanıcı Girişi---------")

kullaniciadi="Burcu"
parola= "256097"

username= input("Kullancı adınızı giriniz: ")
password= input("Parolanızı giriniz: ")

if username==kullaniciadi and password==parola: 
    print("tebrikler başarılı giriş yaptınız.")

elif username!=kullaniciadi and password==parola:
    print("kullanıcıyı adını yanlış girdiniz.")

elif username==kullaniciadi and password!=parola:
    print("şifreyi yanlış girdiniz.")

