#Klavyeden 4 kenarı girilen bilginin kare mi yoksa dikdörtgen mi olduğunu bulan program yazınız

a=int(input("1.Kenarı Giriniz : "))
b=int(input("2.Kenarı Giriniz : "))
c=int(input("3.Kenarı Giriniz : "))
d=int(input("4.Kenarı Giriniz : "))
kare=("Kare")
dikdörtgen=("Dikdörtfen")

if a==b==c==d:
    
    print("Sonuc : ",kare)

elif (a==c and b==d) or (a==b and c==d) or (a==d and c==b):
    print("Sonuc : ",dikdörtgen)

else:
    print("Dörtgen")
