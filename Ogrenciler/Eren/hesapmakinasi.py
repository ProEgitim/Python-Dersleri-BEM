baslik='''
*************************************************************
*         -HESAP MAKİNASI PROGRAMINA HOŞGELDİNİZ-           *
*************************************************************
PROGRAMDAN ÇIKMAK İÇİN 'Q'e BASIN!!!
'''
print(baslik)


print("Yapmak İstediğiniz İşlemi Seciniz\n1)Toplama\t2)Çıkarma\t3)Çarpma\t4)Bölme")  
sec = input("Seçenekler: 1 , 2 , 3 , 4  , q veya Q (çıkış): ")
print()

if sec=="Q" or sec=="q":
    print("Programdan çıkılıyor...İYİ GÜNLER.") 



elif sec == "1":
    print("---->> TOPLAMA İŞLEMİ <<-----")
    a=int(input("1.Sayıyı Giriniz: ")) 
    b=int(input("2.Sayıyı Giriniz: "))
    print("{}  +   {}    =  {}".format(a, b, a+b))  
    print("Toplam Sonuc : ",a+b )
    
 
elif sec == "2":
    print("---->> ÇIKARMA İŞLEMİ <<-----")
    a=int(input("1.Sayıyı Giriniz: ")) 
    b=int(input("2.Sayıyı Giriniz: "))
    print("{}  -   {}    =  {}".format(a, b, a-b))
    print("Fark Sonuc : ",a-b )
elif sec == "3":
    print("---->> ÇARPMA İŞLEMİ <<-----")
    a=int(input("1.Sayıyı Giriniz: ")) 
    b=int(input("2.Sayıyı Giriniz: "))
    print("{}  *   {}    =  {}".format(a, b, a*b))
    print("Çarpma Sonuc : ",a*b )
elif sec == "4":
    print("---->> BÖLME İŞLEMİ <<-----")
    a=int(input("1.Sayıyı Giriniz: ")) 
    b=int(input("2.Sayıyı Giriniz: "))
    print("{}  /   {}    =  {}".format(a, b, a/b))
    print("Bölme Sonuc : ",a/b )



else :
    print("Hatalı Giriş!! Lütfen Ekrandaki Seçenekleri Seçiniz ")
    


