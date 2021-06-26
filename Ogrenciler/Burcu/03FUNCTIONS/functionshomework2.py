

def ebob_bul(say1,say2):
    i=1
    ebob=1
    while(say1>=i and say2>=i):
        if(not(say1 % 1) and not(say2 %i )):
            ebob=i 
        i+=1
    return ebob
a= int(input("sayı 1:"))
b= int(input("sayı 2:"))

print(ebob_bul(a,b))