import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textbox=QtWidgets.QLineEdit()
        self.clean=QtWidgets.QPushButton("Temizle")
        self.print=QtWidgets.QPushButton("Yazdır")
        v_box=QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.textbox)
        v_box.addWidget(self.clean)
        v_box.addWidget(self.print)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clean.clicked.connect(self.click)
        self.print.clicked.connect(self.click)

        self.show()

    def click(self):
        sender=self.sender()
        if sender.text() == "Temizle":
            self.textbox.clear()

        else:
            print(self.textbox.text())

app = QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())



 

   