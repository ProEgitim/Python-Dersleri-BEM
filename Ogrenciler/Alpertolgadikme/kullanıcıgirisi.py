print("------Kullanıcı Gririiş------")
kadi= "Alper"
parola= "12345"

username=input("Kullanıcı Adınızı Gririniz : ")
password=input("Parolanızı Giriniz")

if username== kadi and password==parola :
  print("Giriş Başarılı")

elif username != kadi and password == parola:
  print("Kullanıcı Adı Hatalı") 

elif username==kadi and password != parola:
  print("Parola Hatalı")

elif username != kadi and password != parola:
  print("Kullanıcı adı ve Parola Hatalı")

