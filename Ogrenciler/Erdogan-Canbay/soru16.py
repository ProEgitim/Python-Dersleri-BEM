"""
kullanıcıdan alınan bir sayının tek mi ya da çift mi olduğunu bulan kodu yazınız
"""
sayi=int(input("sayiyi giriniz.."))
if sayi % 2 == 1:
    print(sayi," sayımız tektir..")
elif sayi % 2 == 0:
    print(sayi," sayımız çifttir..")