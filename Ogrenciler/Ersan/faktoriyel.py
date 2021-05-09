while(True):

    sayi = int(input("Bir sayı Giriniz: "))
    fak = 1
    for i in range(2,sayi+1):
        fak*= i
    print("Faktöriyel= ", fak)