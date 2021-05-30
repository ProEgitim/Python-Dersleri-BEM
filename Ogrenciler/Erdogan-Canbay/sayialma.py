birler=["","bir","iki","uc","dort","bes","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

alinandeger = int(input("sayinizi giriniz.."))

def okunus(sayi):
    birlerbasamagi=sayi%10
    onlarbasamagi=sayi//10
    return onlar[onlarbasamagi] + " " + birler[birlerbasamagi]

print(okunus(alinandeger))
