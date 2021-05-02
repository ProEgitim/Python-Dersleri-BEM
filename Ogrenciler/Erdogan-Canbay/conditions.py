"""
if else koşulları
"""
kosul=False;
if (kosul):
    print("koşul doğru")
else:
    print("koşul yanlış")

yas=int(input("yaşını gir.. "))
if yas > 18:
    print("hoşgeldin")
else:
    print("yaş doğrulanmadı")

a=3
b=5
c=8

secim=input("secim yapınız {a b c}.. ")
if(secim == "a"):
    print(a)
elif(secim == "b"):
    print(b)
elif(secim == "c"):
    print(c)
    