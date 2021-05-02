
#     Toplam Not >  90 -----> AA
#     Toplam Not >  85 -----> BA
#     Toplam Not >  80 -----> BB
#     Toplam Not >  75 -----> CB 
#     Toplam Not >  65 -----> DC     
#     Toplam Not >  55 -----> CC
#     Toplam Not <  55 -----> FF
sayi1=int(input("Notunuzu Giriniz : "))
if(sayi1 >90):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("AA")
elif(sayi1>85):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("BA")
elif(sayi1>80):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("BB")
elif(sayi1>75):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("CB")
elif(sayi1>65):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("DC")
elif(sayi1>55):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("CC")
elif(sayi1<55):
    print("Aldıgınız Harf Notu: ")
    print(sayi1)
    print("FF")
else:
    print("Kaldınız")

