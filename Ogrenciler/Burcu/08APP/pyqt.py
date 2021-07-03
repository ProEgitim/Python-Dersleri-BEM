import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 ilk penceremiz")
    
    e1=QtWidgets.QLabel(pencere)
    e2=QtWidgets.QLabel(pencere)

    e2.setPixmap(QtGui.QPixmap("C:/Users/burcu/Documents/GitHub/Python-Dersleri-BEM/Ogrenciler/Burcu/application-development-with-python.png"))

    e1.setText("Bu bir yazı etiketidir")

    button= QtWidgets.QPushButton(pencere)
    button.setText("Bu bir butondur")

    e1.move(200,30)
    e2.move(100,100)
    button.move(200,60)

    pencere.setGeometry(100,100,500,500,200,60)

    
    pencere.show()
    sys.exit(app.exec_())

Pencere()
