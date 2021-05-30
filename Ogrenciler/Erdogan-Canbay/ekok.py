def okek(say1,say2):
    i=2
    ekok=1
    while(True):
        if((say1 % i == 0) and (say2 % i == 0)):
            say1= say1 / i
            say2 = say2 / i
            ekok *= i
            if(say1 == 1):
                ekok *= i
            if(say2 == 1):
                ekok *= i
        elif(not(say1 % i == 0) and (say2 % i == 0)):
            i+=1
        return ekok

print(okek(8,12))