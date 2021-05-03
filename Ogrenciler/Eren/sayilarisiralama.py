#Girilen 5 sayıdan en büyüğünü gösteren  programı yazınız.

a=int(input("1.Sayiyi Giriniz: "))
b=int(input("2.Sayiyi Giriniz: "))
c=int(input("3.Sayiyi Giriniz: "))
d=int(input("4.Sayiyi Giriniz: "))
e=int(input("5.Sayiyi Giriniz: "))

if (a>=b) and (a>=c) and (a>=d) and (a>=e):
   buyuksayi = a
   
elif (b>=a) and (b>=c) and (b>=d) and (b>=e):
   buyuksayi = b
elif (c>=a) and (c>=b) and (c>=d) and (c>=e):
   buyuksayi = c
elif(d>=a) and (d>=b) and (d>=c) and (d >=e):
   buyuksayi = d
else:
    buyuksayi=e
print(a,",",b,",",c,",",d,"Ve",e,"içinde büyük olan sayı >>>>>",buyuksayi)





