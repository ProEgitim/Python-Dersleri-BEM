def obeb(say1,say2):
    i=1
    ebob=1
    while(say1>=i and say2>=i):
        if(not(say1 % i) and not(say2 % i)):
            ebob=i
        i+=1
    return ebob

alinandeger = int(input("sayi 1 i  giriniz.. "))
alinandeger2 = int(input("sayi 2 yi giriniz.. "))

print(obeb(alinandeger,alinandeger2))