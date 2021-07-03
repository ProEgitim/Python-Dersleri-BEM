import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    
    okay= QtWidgets.QPushButton("Okay")
    cancel= QtWidgets.QPushButton("Cancel")

    h_box= QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    pencere.show()
    sys.exit(app.exec_())

Pencere()