print("""\nMükemmel Sayıyı Bulma Programı
--------------------------------------""")

sayi = int(input("Lütfen bir sayı giriniz: "))
toplam = 0

for i in range(1,sayi):
    if (sayi %i == 0):
        toplam += i

if (sayi == toplam):
    print("Bu Mükemmel Sayıdır")
else:
    print("Bu Mükemmel Sayı Değildir")