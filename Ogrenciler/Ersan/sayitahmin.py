from random import randint
print("""Sayı Tahmin Oyunu
--------------------------
""")


rand = randint (1,100)
sayac = 0

while True:
    sayac += 1
    sayi=int(input("Lütfen 1 ile 100 arasında bir sayı giriniz: "))
    if (sayi == 0):
        print("Oyunu iptal ettiniz")
        break
    elif(sayi< rand):
        print("Lütfen daha yüksek bir sayı giriniz")
        continue
    elif (sayi > rand):
        print("Lütfen daha düşük bir sayı giriniz")
        continue
    else:
        print("Rastgele seçilen sayı {}".format(rand))
        print("Tahmin sayınız {}".format(sayac))
