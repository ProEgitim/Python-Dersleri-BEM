class Animal():

    def __init__(self, a, b):
        self.name = a
        self.age = b 

    def getAge(self):
        print(self.age)
    def getName(self):
        print(self.name)

a1 = Animal("dog", 2)
a2 = Animal("cat", 1)
a3 = Animal("pig", 4)    
a4 = Animal("turtle", 100) 

a4.getName
a4.getAge
print("....................")
a2.getName()
a2.getAge()
print("....................")
a1.getName()
a1.getAge()
print("....................")
a3.getName()
a3.getAge()

### Get name dedğimiz de niçin return yapmadık; çlaıştırdığımda çalışmıyor.
### Yan yana yazmak istiyorum nasıl yapabilirim.