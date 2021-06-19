def notHesapla(satir):
    satir=satir[:-1]
    liste=satir.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    ortalama=not1*0.3+not2*0.3+not3*0.4
    if (ortalama >= 90):
        harfNotu="AA"
    elif(ortalama >= 85):
        harfNotu="BA"
    elif(ortalama >= 80):
        harfNotu="BB"
    elif(ortalama >= 75):
        harfNotu="CB"
    elif(ortalama >= 70):
        harfNotu="CC"
    elif(ortalama >= 65):
        harfNotu="DC"
    elif(ortalama >= 60):
        harfNotu="DD"
    elif(ortalama >= 55):
        harfNotu="FD"
    else:
        harfNotu="FF"
    return isim + "-------->"+harfNotu+"\n"
with open("dosya.txt","r",encoding="utf-8") as file:
    ortalamaListesi=[]
    for i in file:
        ortalamaListesi.append(notHesapla(i))
    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in ortalamaListesi:
            file2.write(i)