
print("""
ATM'ye hoşgeldiniz
-------------------------------

Yapabileceğiniz İşlemler
    1. Bakiye sorma
    2. Para Yatırma
    3. Para Çekme

Programdan q ile çıkabilirsiniz
""")

i = 1000

while(True):
    islem= input("Lütfen yapmak istediğiniz işlem numarasını giriniz: ")

    if (islem == "1"):
        print(i)
        continue
    elif (islem == "2"):
        para=int(input("Yatıracağınız para miktarını giriniz:"))
        i = i+para
        print(i)
    elif (islem == "3"):
        para=int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
        
        if (i == 0):
            print("para yetersiz")
            continue
        i = i-para
        print(i)
    elif (islem == "q"):
        print("Programdan çıkılıyor.")
        break
    else:
        print("lütfen geçerli bir işlem giriniz.")