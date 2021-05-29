#1'den 100'e kadar olan çift sayıları listeye atalım.

even=[]
for n in range(1,101):
    if n%2==0:
        even.append(n)
print(even)