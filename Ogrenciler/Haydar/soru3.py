# Soru: Kullanıcıdan iki tane sayı alın ve bu sayıların değerlerini birbirleri ile değiştirin
#Cevap:

a=int= input("Birinci sayı girin:")
b=int= input("ikinci sayı girin:")
a, b = b, a
print("{} {}".format(a,b))