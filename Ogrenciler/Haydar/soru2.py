# Soru: Kullanıcıdan aldığımız boy ve kilo değerine göre beden kitle indexsini bulun. BDI=kilo/boy*boy
#Cevap:
boy=float (input("Boyunuzu giriniz:"))
kilo=int (input("kilonuzu giriniz:"))
print("Beden kitle indeksiniz:",kilo/(boy**2))