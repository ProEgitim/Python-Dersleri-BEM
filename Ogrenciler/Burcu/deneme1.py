kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız : ")
toplam_uzunluk = len(kullanıcı_adı) + len(parola)

mesaj="toplam uzunluk {} karakterden oluşuyor."

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk > 20:
    print("Yok artık daha neler!")
elif toplam_uzunluk == 20:
    print("woow sende yine iyisin.")
else:
    print("tamam oldu işte ne gerek var zaten çok karaktere.")
