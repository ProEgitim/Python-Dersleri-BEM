"""
c=(a**2+b**2)**0.5

"""

def pisagorBul():
    pisagorListesi=list()

    for a in range(1,101):
        for b in range(1,101):
            c=(a**2+b**2)**0.5
            if(c==int(c)):
                pisagorListesi.append((a,b,int(c)))
    return pisagorListesi


for i in pisagorBul():
    print(i)