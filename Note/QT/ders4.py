import sys
import sqlite3
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.getSQL()
        self.initUI()
    def getSQL(self):
        db=sqlite3.connect("data.db")
        self.cursor=db.cursor()
        self.cursor.execute(" Create Table If not exists uyeler(userName TEXT, password TEXT)")
        db.commit()
    def initUI(self):
        self.userName=QtWidgets.QLineEdit()
        self.password=QtWidgets.QLineEdit()
        self.loginButton=QtWidgets.QPushButton("Giriş")
        self.textLabel=QtWidgets.QLabel("")
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.userName)
        v_box.addWidget(self.password)
        v_box.addWidget(self.textLabel)
        v_box.addStretch()
        v_box.addWidget(self.loginButton)
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.loginButton.clicked.connect(self.login)
        self.show()
    def login(self):
        name=self.userName.text()
        pw=self.password.text()
        self.cursor.execute("Select * from uyeler where userName = ? and password = ?",(name,pw))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.textLabel.setText("Yanlış Giriş Yaptını!")
        else:
            self.textLabel.setText("Hoş Geldiniz.")
app = QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())