import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("İptal")
    textbox=QtWidgets.QLineEdit()
    h_box= QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addWidget(textbox)
    h_box.addStretch()

    v_box=QtWidgets.QVBoxLayout()
    
    v_box.addStretch()
    v_box.addLayout(h_box)
    v_box.addStretch()

    pencere.setGeometry(100,100,500,500)
    pencere.setLayout(v_box)

    pencere.show()
    sys.exit(app.exec_())

Pencere()