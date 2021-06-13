class Square(object):
    side = 6
    area = 0
   
    def area(self):
        self.area = self.side * self.side
        print("Area:", self.area)

s1 = Square()
print(s1.side)
print(s1.area())
