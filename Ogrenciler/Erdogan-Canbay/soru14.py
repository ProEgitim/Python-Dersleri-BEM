"""
Klavyeden 4 kenarı girilen bilginin kare mi yoksa dikdörtgen mi olduğunu bulan program yazınız.---Eren Özdemir
"""

kenar1=int(input("1.kenarı giriniz.."))
kenar2=int(input("2.kenarı giriniz.."))
kenar3=int(input("3.kenarı giriniz.."))
kenar4=int(input("4.kenarı giriniz.."))

if kenar1==kenar2 or kenar1==kenar3 or kenar1==kenar4:
    if kenar1==kenar3:
        if kenar1==kenar4 and kenar2==kenar3:
            print("bu bir kare")
        else:
            print("bu bir dikdörtgen")
    else:
        print("bu bir dikdörtgen")
else:
    print("bu tam bir yamuk")