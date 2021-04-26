#Kullanıcının girdiği key:value girdilerine göre bir sözlük programı oluşturun.
Anahtar=str(input("Anahtar Kelimeyi Yazınız : "))
Deger=str(input("Anahtar Kelimenin Değeri : "))
sozluk = {Anahtar:Deger}
print("Elemanlar : >>>>>>>",sozluk.items())
print("Girilen Kelime : >>>>>>>",sozluk.keys())
print("Girilen Değer : >>>>>>>",sozluk.values())
print("Sınıf Türü : >>>>>>>",type(sozluk))
print("\nElemanlar;",sozluk)
print(Anahtar,  "= Anahtar Kelime : ",len(sozluk))
print(Deger,  "= Anahtar Kelimenin Değeri : ",len(sozluk))
print(Anahtar,  "= Anahtar Kelimede Toplam",len(Anahtar),"harf var.")
print(Deger,  "= Anahtar Kelimede Toplam",len(Deger),"harf var.")
print("Sınıf Türü : ",type(len(sozluk)))






