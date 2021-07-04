django - todo-app
Proje klasörü içinde:

pip install virtualenv

virtualenv myenv --isimverip env oluşturuyor)

c:\w\django\myenv\Scripts\activate.bat --yolu dosya yoluna göre)

pip install django

django-admin startproject todo_project --proje oluştur

cd todo_project

python manage.py runserver

http://127.0.0.1:8000/
Migration:

python manage.py migrate
Kullanıcı Oluştur:

app dizininde:

python manage.py createsuperuser
todo uygulaması için:

python manage.py startapp todo_app
model.py deki değişikliklerin veritabanına yazılması için:

python manage.py makemigrations python manage.py migrate
Örnekteki dosyayı kullanmak için:

kurmuş olduğunuz env ile aynı klasör içine atıp env çalıştırıp sunucunuzu başlatabilirsiniz.