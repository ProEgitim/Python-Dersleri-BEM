"""
liste=degisken.split(" ")
"""
def kontrol(str):
    sayac=0
    liste=str.split(" ")
    for i in liste:
        if i == "ve":
            sayac+=1
    if sayac==1:
        return True
    else:
        return False

metin=input("Metni giriniz:")
if (kontrol(metin)):
    print("girdiniz metinde ve kelimesi bulundu")
else:
    print("girdiniz metinde ve kelimesi bulunamadı")