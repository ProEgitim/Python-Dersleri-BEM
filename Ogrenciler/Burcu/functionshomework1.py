
##6 bir mükemmel sayıdır. Çünkü 6’nın pozitif bölenleri 1,2,3 ve 6’dır. 
# Kendisi hariç diğer bölenlerini toplarsak 1+2+3=6 eder.###


def mukemmel(sayi):
    rakam=0
    for i in range(1,sayi):
        if sayi%i==0:
            rakam+=i
    if rakam==sayi:
        print (sayi," mukemmel sayidir.")
    else:
        print (sayi," mukemmel sayi degildir")

sayi=int(input("sayi giriniz:"))
mukemmel(sayi)
sayi=int(input("sayi giriniz:"))
mukemmel(sayi)
sayi=int(input("sayi giriniz:"))
mukemmel(sayi)
sayi=int(input("sayi giriniz:"))
mukemmel(sayi)
sayi=int(input("sayi giriniz:"))
mukemmel(sayi)