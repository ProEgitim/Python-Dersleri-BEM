"""
Kullanıcıdan alınan iki sayı ile yine kullanıcının seçtiği işlemi yapacak hesap makinası programını yazınız.
"""

sayi1=int(input("1.sayiyi giriniz.."))
sayi2=int(input("2.sayiyi giriniz.."))
islem=input("işlemi seçiniz + - * / ..")

if islem == "+":
    sonuc=sayi1+sayi2
elif islem == "-":
    sonuc = sayi1-sayi2
elif islem=="*":
    sonuc = sayi1*sayi2
elif islem == "/":
    sonuc = sayi1/sayi2

print("{}{}{}={}".format(sayi1,islem,sayi2,sonuc))   