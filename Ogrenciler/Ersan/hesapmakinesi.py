print("\n-------------------------")
print("\nHesap Makinesi")
print("\n-------------------------")
print("\nLütfen yapmak istediğiniz işlemi seçiniz")
print("\nToplama İşlemi için lütfen 1'e basınız")
print("Çıkartma İşlemi için lütfen 2'ye basınız")
print("Çarpma İşlemi için lütfen 3'e basınız")
print("Bölme İşlemi için lütfen 4'e basınız")
islem = int(input("\nLütfen işlem numarasınız giriniz: "))

    

if (islem == 1):
    sayi1=int(input("\nLütfen ilk sayıyı giriniz: "))
    sayi2=int(input("\nlütfen ikinci sayıyı giriniz: "))
    sonuc = sayi1 + sayi2
    print("\n{} + {} = {}".format(sayi1,sayi2,sonuc))

    
elif (islem == 2):
    sayi1=int(input("\nLütfen ilk sayıyı giriniz: "))
    sayi2=int(input("\nlütfen ikinci sayıyı giriniz: "))
    
    sonuc = sayi1 - sayi2
    print("\n{} - {} = {}".format(sayi1,sayi2,sonuc))
    
elif (islem == 3):
    sayi1=int(input("\nLütfen ilk sayıyı giriniz: "))
    sayi2=int(input("\nlütfen ikinci sayıyı giriniz: "))
    sonuc = sayi1 * sayi2
    print("\n{} x {} = {}".format(sayi1,sayi2,sonuc))
    
elif (islem == 4):
    sayi1=int(input("\nLütfen ilk sayıyı giriniz: "))
    sayi2=int(input("\nlütfen ikinci sayıyı giriniz: "))
    sonuc = sayi1 / sayi2
    print("\n{} / {} = {}".format(sayi1,sayi2,sonuc))
    
else:
    print("\nLütfen sizden istenilen aralıklarda bir sayı giriniz.")
        