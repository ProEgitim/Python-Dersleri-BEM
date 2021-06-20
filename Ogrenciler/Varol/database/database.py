import sqlite3
database=sqlite3.connect("data.db")
imlec=database.cursor()
def tabloOlustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik(Isim TEXT, Yazar TEXT, Yayinevi TEXT, SayfaSayisi INT)")
    database.commit()
def degerEkle(isim,yazar,yayinevi,sayfaSayisi):
    imlec.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfaSayisi))
    database.commit()
def tumVerileriAl():
    imlec.execute("Select * From kitaplik")
    data=imlec.fetchall()
    print("Kitaplık Tablosu Bilgileri:")
    for i in data:
        print(i)
def isimYazar():
    imlec.execute("Select Isim,Yazar From kitaplik")
    data=imlec.fetchall()
    print("İsim ve Yazar Bilgileri:")
    for i in data:
        print(i)
def yayineviGetir(yayinevi):
    imlec.execute("Select * From kitaplik where Yayinevi = ?",(yayinevi,))
    data=imlec.fetchall()
    print("Yayınevine göre tablo bilgileri:")
    for i in data:
        print(i)
def veriGuncelle(onceki,sonraki):
    imlec.execute("Update kitaplik set Yayinevi = ? where Yayinevi = ?",(sonraki,onceki))
    database.commit()
def veriSil(yazar):
    imlec.execute("Delete From kitaplik where Yazar = ?",(yazar,))
    database.commit()
# isim=input("İsim:")
# yazar=input("Yazar:")
# yayinevi=input("Yayınevi:")
# sayfaSayisi=int(input("Sayfa Sayısı:"))
# tabloOlustur()
# degerEkle(isim,yazar,yayinevi,sayfaSayisi)
# tumVerileriAl()
# isimYazar()
# yayineviGetir('BEM')
veriGuncelle('BEM','Everest')
silinecekYazar=input("Silinecek yazarı girin:")
veriSil(silinecekYazar)
database.close()