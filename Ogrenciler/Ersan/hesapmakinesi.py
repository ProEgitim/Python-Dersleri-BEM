print("Hesap Makinesi")
print("-------------------------")
print("Lütfen yapmak istediğiniz işlemi seçiniz")
print("Toplama İşlemi için 1'e basın")
print("Çıkartma İşlemi için 2'y2 basın")
print("Çarpma İşlemi için 3'e basın")
print("Bölme İşlemi için 4'e basın")
islem = int(input("Lütfen işlem numarasınız giriniz: "))
sayi1=int(input("Lütfen ilk sayıyı giriniz: "))
sayi2=int(input("lütfen ikinci sayıyı giriniz: "))
if (islem == 1):
    sonuc = sayi1 + sayi2
    print("{} + {} = {}".format(sayi1,sayi2,sonuc))
elif (islem == 2):
    sonuc = sayi1 - sayi2
    print("{} - {} = {}".format(sayi1,sayi2,sonuc))
elif (islem == 3):
    sonuc = sayi1 * sayi2
    print("{} x {} = {}".format(sayi1,sayi2,sonuc))
elif (islem == 4):
    sonuc = sayi1 / sayi2
    print("{} / {} = {}".format(sayi1,sayi2,sonuc))
else:
    print("Lütfen İstenilen sayıları giriniz")
        