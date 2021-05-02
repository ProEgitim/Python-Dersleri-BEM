a=int(input("notunuzu giriniz:"))
sonuc=""
if (a>=90):
    sonuc="AA"
elif (a>=85):
    sonuc="BA"
elif (a>=80):
    sonuc="BB"
elif (a>=75):
    sonuc="CB"
elif (a>=65):
    sonuc="DC"
elif (a>=55):
    sonuc="CC"
else: 
    sonuc="FF"

if (sonuc=="FF"):
    print(sonuc,"ile kaldınız")
else:
    print("Tebrikleri geçtiniz, harf notunuz:",sonuc)