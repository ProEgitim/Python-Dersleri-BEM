print("\nHoşgeldiniz")

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))
sayi4 = int(input("4. Sayı: "))
sayi5 = int(input("5. Sayı: "))
 
if (sayi1 >= sayi2) and (sayi1 >= sayi3) and (sayi1 >=sayi4) and (sayi1 >=sayi5):
   buyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3) and (sayi2 >= sayi5) and (sayi2 >=sayi4):
   buyuk = sayi2
elif (sayi3 >= sayi4) and (sayi3 >= sayi5) and (sayi3 >= sayi2) and (sayi3 >=sayi1):
    buyuk = sayi3
elif (sayi4 >= sayi5) and (sayi4 >= sayi2) and (sayi4 >= sayi3) and (sayi4 >=sayi1):
    buyuk = sayi4
elif (sayi5 >= sayi4) and (sayi5 >= sayi2) and (sayi5 >= sayi3) and (sayi5 >=sayi1):
    buyuk = sayi5

 
print(sayi1,",",sayi2, ",",sayi3, ",",sayi4,"," ,"ve",",",sayi5,",","içinde büyük olan sayı",buyuk)