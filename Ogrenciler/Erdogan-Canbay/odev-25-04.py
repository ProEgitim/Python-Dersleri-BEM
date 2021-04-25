"""
Odev_25 nisan = kullanıcının girdiği key:value girdilerine göre bir sözlük programı oluşturun.
"""
Anahtar=str(input("Key değeri giriniz.."))
Deger=str(input("Value değerini giriniz.."))

sozluk={Anahtar:Deger}
print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())
print(type(sozluk))