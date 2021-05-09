
print("""
ATM'ye hoşgeldiniz
-------------------------------

Yapabileceğiniz İşlemler
    1. Bakiye sorma
    2. Para Yatırma
    3. Para Çekme

Programdan q ile çıkabilirsiniz
""")

bakiye = 1000

while True:
    islem= input("Lütfen yapmak istediğiniz işlem numarasını giriniz: ")
    if (islem == "1"):
        print(bakiye)
    elif (islem == "2"):
        para=int(input("Yatıracağınız para miktarını giriniz:"))
        bakiye = bakiye+para
        print(bakiye)
    elif (islem == "3"):
        para=int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
        if (bakiye - miktar < 0 ):
            print("para yetersiz")
            continue
        bakiye = bakiye-para
        print(bakiye)
    elif (islem == "q"):
        print("Programdan çıkılıyor.")
        break
    else:
        print("lütfen geçerli bir işlem giriniz.")