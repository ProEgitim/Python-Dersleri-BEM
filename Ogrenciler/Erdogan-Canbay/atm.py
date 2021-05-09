print("""
    Atm ye hoşgeldiniz..
    1.bakiye sorma
    2.para yatırma
    3.para çekme

    çıkmak için q ya basınız..

""")

bakiye =1000
while True:
    secim=input("Seciminizi yapınız.. ")

    if secim == "1":
        print("bakiyeniz ",bakiye)
    if secim == "2":
        print("Para yatırma işlemine hoş geldiniz..")
        yatir=int(input("yatiracagınız miktarı giriniz.. "))
        bakiye += yatir
        print("Mevcut Bakiyeniz ",bakiye)
    if secim == "3":
        print("Para çekmek istediğinize emin misiniz ? ")
        cek=int(input("Cekeceğin miktarı yaz "))
        if cek > bakiye:
            print("Bakiye yetersiz yeniden deneyin")
            continue
        bakiye -= cek
        print("Kalan bakiye ",bakiye)
    if secim == "q":
        break
print("yine bekleriz")
        