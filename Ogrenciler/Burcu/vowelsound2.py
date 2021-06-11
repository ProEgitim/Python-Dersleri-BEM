sesli_harfler = 'aeıioöuü'
rakam = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler
for harf in kelime:
    if seslidir(harf):
        rakam += 1
mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, rakam))