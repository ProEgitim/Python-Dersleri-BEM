def kontrol(kelime):
    print("kelimemiz.. "+kelime)
    liste=kelime.split(" ")
    return liste

giris=input("kelimeyi giriniz.. ")

bulundu =kontrol(giris)
print(bulundu)

for i in bulundu:
   if(i == "ve"):
       print("ve bulundu")
   elif(i != "ve"):
        print("ve bulunamadı")