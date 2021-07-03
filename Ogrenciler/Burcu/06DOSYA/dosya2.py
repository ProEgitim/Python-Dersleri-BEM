###dosya = open ("mybooks.txt" , "w")
###dosya.close()

"""file = open ("file1.txt", "w" , encoding="utf-8")
file.write(" The books I read of The Month")
file.close()"""

""""file = open ("file1.txt", "r" , encoding="utf-8")
file.close()"""

file = open ("file1.txt", "a" , encoding="utf-8")

file.write("Homo sapiens\n")
file.write("Sandman\n")
file.write("Sıradan Zaferler\n")
file.write("İyimser olmayan Umut\n")
file.write("blink\n")

print(file)

for i in file:
    print(i)
file.close()

""" Bozuk bir şekilde alt alta sıralıyor"""











