import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQT5 ilk penceremiz")

    e1=QtWidgets.QLabel(pencere)
    e2=QtWidgets.QLabel(pencere)

    e2.setPixmap(QtGui.QPixmap("C:/Users/nabru\Documents/Github/Python-Dersleri-BEM/Note/QT/python.png"))

    e1.setText("Bu bir yazı etiketidir.")

    buton= QtWidgets.QPushButton(pencere)
    buton.setText(" Bu bir butondur")

    e1.move(200,30)
    e2.move(120,100)
    buton.move(200,60)

    pencere.setGeometry(100,100,500,500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()