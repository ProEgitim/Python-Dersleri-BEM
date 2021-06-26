class Programmer():
    def __init__(self, name, surname, register, salary, language):
        self.name= name
        self.surname= surname
        self.register= register
        self.salary= salary
        self.language= language

    def getinfo(self):
        print("""
        
        Employee Info
        
        Name: {}
        
        Surname: {}

        Register {}

        Salary {}
        
        Languages {}
        
        """.format(self.name, self.surname,self.register, self.salary,self.language))

    def addLanguage(self,newlang):
        print("adding new language...")
        self.language.append(newlang)

    def raiseSalary(self,increasemoney):
        print("Your Salary is increasing...")
        self.salary+=increasemoney

programmer1 = Programmer("Burcu", "Willow", 156987, 16000,["Python","C"])
programmer1.addLanguage("go")
programmer1.raiseSalary(600)
programmer1.getinfo()