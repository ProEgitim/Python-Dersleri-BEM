"""
Girilen 5 sayıdan en büyüğünü gösteren programı yazınız.
"""
sayilar=[];
for i in range(0,5):
    sayi=int(input("sayiyi giriniz.."))
    sayilar.append(sayi)
sayilar.sort()
print("En büyük sayimiz..",sayilar[-1])