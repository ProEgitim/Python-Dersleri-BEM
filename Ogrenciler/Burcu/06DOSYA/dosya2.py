###dosya = open ("mybooks.txt" , "w")
###dosya.close()

"""file = open ("file1.txt", "w" , encoding="utf-8")
file.write(" The books I read of The Month")
file.close()"""

""""file = open ("file1.txt", "r" , encoding="utf-8")
file.close()"""

file = open ("file1.txt", "r" , encoding="utf-8")

file.write("Homo sapiens")
file.write("Sandman")
file.write("Sıradan Zaferler")
file.write("İyimser olmayan Umut")
file.write("blink")

print(file)

for i in file:
    print(i, end="    ")

""" Bozuk bir şekilde alt alta sıralıyor"""











