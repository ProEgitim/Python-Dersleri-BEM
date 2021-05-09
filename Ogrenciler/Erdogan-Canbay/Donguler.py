"""in operatoru içinde olup olmadıgına bakar"""

liste = [1,2,3,4,5,6,7,8,9]
for eleman in liste:
    print("Eleman: ",eleman)

toplam=0
for e in liste:
    toplam += e
print("toplam: ",toplam)

for sayi in liste:
    if(sayi % 2 == 0):
        print(sayi," sayimiz çift")
    else:
        print(sayi," sayimiz tek")

karekterler="Erdogan"
for item in karekterler:
    print(3*item)

"""
while döngüsü
"""
x=0
while(x<10):
    print("x in degeri ",x)
    x+=1

a=0
while(a<len(liste)):
    print("index: ",a," Eleman",liste[a])
    a+=1