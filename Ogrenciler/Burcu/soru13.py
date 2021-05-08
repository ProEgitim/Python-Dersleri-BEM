
secim=input("İşlem seçin: (a=+,b=-,c=*,d=/)")
sayi1=int(input("1.sayı: "))
sayi2=int(input("2.sayı: "))

if (secim == "a") :
    print(sayi1, "+", sayi2, "=", sayi1+sayi2)
elif (secim == "b") : 
    print(sayi1, "-", sayi2, "=", sayi1-sayi2)
elif (secim== "c") :
    print(sayi1, "*", sayi2, sayi1*sayi2)
elif (secim== "d") :
    print(sayi1, "/", sayi2, sayi1/sayi2)