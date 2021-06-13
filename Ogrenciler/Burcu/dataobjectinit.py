class Animal(object):

    def __init__(self, a, b):
        self.name = a
        self.age = b 

    def getAge(self):
        return self.age
    def getName(self):
        print(self.Name)

a1 = Animal("dog", 2)
a2 = Animal("cat", 1)
a3 = Animal("pig", 4)    
a4 = Animal("turtle", 100) 

### Get name dedğimiz de niçin return yapmadık; çlaıştırdığımda çalışmıyor.
