#kullanıcıdan dairenin alanını  ve çevresini hesaplayan bir algoritma oluşturalım.
#Dairenin Alanı =>   π x r2 
#Dairenin Çevresi=>  C = πd
yaricap = float(input("Dairenin Yarıçapını Giriniz:"))
r=yaricap
pi=3.14
Alan=pi*(r**2)
Cevre=2*pi*r
print("\nDairenin Alanı : ",Alan )
print("Dairenin Çevresi : ",Cevre)
print("(π=3.141592653589793)")