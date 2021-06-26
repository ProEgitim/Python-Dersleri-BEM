#1'den 100'e kadar olan ve 3e tam bölünen sayıları bulunuz ?
# i=1
# while(i<100):
#     if (i%3==0):
#         print("i:", i)
#     i+=1
#     continue
    
for i in range(1,101):
    if(i%3!=0):
        continue
    print(i)

