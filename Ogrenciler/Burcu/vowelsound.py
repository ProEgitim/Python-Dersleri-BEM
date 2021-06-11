sesli_harfler = 'aeıioöuü'
toplam = 0

kelime = input('Bir kelime girin: ')
for harf in kelime:
    if harf in sesli_harfler:
        toplam += 1
mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, toplam))