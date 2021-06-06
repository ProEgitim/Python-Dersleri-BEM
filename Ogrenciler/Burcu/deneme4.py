import module1
firstNumber= int(input("Birinci sayıyı girin:"))
secondNumber= int(input("Ikinci sayıyı girin:"))
selectx= input("işlem seçin (toplama: 1, çıkarma: 2, çarpma: 3, bölme: 4:)")
if selectx=="1":
    print("sonuç:", module1.topla(firstNumber, secondNumber))
elif (selectx=="2"):
    print("sonuç:", module1.cıkarma(firstNumber,secondNumber))
elif (selectx=="3"):
    print("sonuç:", module1.carpma(firstNumber,secondNumber))
elif (selectx=="4"):  
    print("sonuç:", module1.bolme(firstNumber,secondNumber))
else:
    print("Yanlış seçim yaptınız.")  
