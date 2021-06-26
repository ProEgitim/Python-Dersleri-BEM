birler=["", "bir","iki","üç","dört","beş","altı","sekiz","dokuz"]
onlar=["" ,"on","yirmi","otuz", "kırk","elli","altmış","yetmiş","seksen","doksan",]

alinandeger = int(input("sayınızı giriniz:"))

def okunus(sayi):
    birlerbasamagi=sayi % 10
    onlarbasamagi = sayi // 10

    return onlar[int(onlarbasamagi)] + " " + birler[birlerbasamagi]

print(okunus(alinandeger))
