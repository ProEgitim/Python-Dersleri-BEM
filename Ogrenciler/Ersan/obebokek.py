sayi1= int(input("LÜtfen birinci sayıyı giriniz: "))
sayi2= int(input("Lütfen İkinci sayıyı giriniz: "))

a = max(sayi1, sayi2)

obeb = 1
okek = 1


for i in range (1 , a):

    if sayi1 % i == 0 and sayi2 % i == 0:
        obeb = obeb * i

        sayi1 = sayi1 / i
        sayi2 = sayi2 / i

okek = sayi1 * sayi2 * obeb

print("Gridiğiniz değerlere ait okek: ", okek)
print("girdiğiniz değerlere ait obeb: ",obeb)

