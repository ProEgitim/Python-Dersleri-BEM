"""
kullanıcıdan aldıgımız boy ve kg değerlerine göre beden kitle hesabı
kilo/boy*boy
"""
boy:float=float(input("boy= "))
kilo:float=float(input("kilo= "))

print("sonuc= ")
bdi=float((kilo/(boy*boy)))
print(bdi)

if bdi >25:
    print("şişman reyis")