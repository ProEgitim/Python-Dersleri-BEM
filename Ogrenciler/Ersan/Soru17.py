
dongu = True
while (dongu):
    sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
    sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))
    print("""LÜtfen yapmak istediğiniz İşlemi Seçiniz
    Toplama için  1
    Çıkartma için 2
    Çarpma için   3
    Bölme için    4 """)
    islem = (input("LÜtfen yapmak istediğiniz işlemi seçiniz: "))

    if (islem == 1):
            
        print("{} + {} = {} dır.".format(sayi1,sayi2, sayi1 + sayi2))
        
    elif (islem == 2):
        
        print("{} ile {} 'nin farkı {} dır.".format(sayi1,sayi2, sayi1 - sayi2))
    
    elif (islem == 3):
        
        print("{} ile {} 'nin çarpımı {} dır.".format(sayi1,sayi2, sayi1 * sayi2))
    
    elif (islem == 4):
        
        print("{} ile {} 'nin bölümü {} dır.".format(sayi1,sayi2, sayi1 / sayi2))
    
    else:
        
        print("Lütfen sizden istenen işlemlerden birini seçiniz..!")
    
    devam = input("Devam etmek isterseniz [Evet : e, Hayır : h]")


    if (devam.lower() == "e"):
        dongu = True
    elif (devam.lower() == "h"):
        dongu = False
    else:
        print("LÜtfen seçimlerinizi kontrol ediniz..!")
    
