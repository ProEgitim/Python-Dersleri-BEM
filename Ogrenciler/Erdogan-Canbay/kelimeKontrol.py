def kontrol(kelime):
    print("kelimemiz.. "+kelime)
    liste=kelime.split(" ")
    return liste

giris=input("kelimeyi giriniz.. ")

listem =kontrol(giris)
print(listem)

for i in listem:
    if(i == "ve"):
        bulundu=True
        break
    else:
        bulundu=False

if(bulundu):
    print("ve bulundu")
else:
    print("ve bulunamadı")