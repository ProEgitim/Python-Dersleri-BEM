def ekok_bulma(say1,say2):
    i=2
    ekok=1
    while(True):
        if(say1 % i == 0 and say2 % i == 0):
            ekok*=i
            say1//=i 
            say2//=i
        elif(say1 % i == 0 and say2 % i != 0):
            ekok*=i
            say1//=i
        elif(say1 % i != 0 and say2 % i == 0):
            ekok*=i
            say2//=i

        else:
            i+=1
        if(say1==1 and say2==1):
            break
    return ekok

a=int(input("say 1 i giriniz:"))
b=int(input("say 2 i giriniz:"))

print(ekok_bulma(a,b))


        
    

