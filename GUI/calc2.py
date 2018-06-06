# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import (QTextEdit, QPushButton,  QApplication, QWidget)
from PyQt5.QtCore import (Qt,QRect)

class Window(QWidget):
    
    global num
    num=0

    def __init__(self):
        super().__init__()


        self.init_ui()

    def init_ui(self):
        self.resize(400, 380)
        
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setText('4')
        self.pushButton_4.setGeometry(QRect(10, 170, 51, 61))
        

        self.pushButton_1 = QPushButton(self)
        self.pushButton_1.setText('1')
        self.pushButton_1.setGeometry(QRect(10, 230, 51, 61))

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setText('2')
        self.pushButton_2.setGeometry(QRect(60, 230, 51, 61))

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setText('5')
        self.pushButton_5.setGeometry(QRect(60, 170, 51, 61))

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setText('3')
        self.pushButton_3.setGeometry(QRect(110, 230, 51, 61))

        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setText('6')
        self.pushButton_6.setGeometry(QRect(110, 170, 51, 61))

        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setText('7')
        self.pushButton_7.setGeometry(QRect(10, 110, 51, 61))

        self.pushButton_8 = QPushButton(self)
        self.pushButton_8.setText('8')
        self.pushButton_8.setGeometry(QRect(60, 110, 51, 61))

        self.pushButton_9 = QPushButton(self)
        self.pushButton_9.setText('9')
        self.pushButton_9.setGeometry(QRect(110, 110, 51, 61))

        self.pushButton_0 = QPushButton(self)
        self.pushButton_0.setText('0')
        self.pushButton_0.setGeometry(QRect(10, 290, 51, 61))

        self.pushButton_d = QPushButton(self)
        self.pushButton_d.setText('.')
        self.pushButton_d.setGeometry(QRect(60, 290, 51, 61))

        self.pushButton_e = QPushButton(self)
        self.pushButton_e.setText('9')
        self.pushButton_e.setGeometry(QRect(110, 290, 51, 61))

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(10, 10, 361, 75))

        self.pushButton_c = QPushButton(self)
        self.pushButton_c.setText('C')
        self.pushButton_c.setGeometry(QRect(320, 110, 51, 61))

        self.pushButton_ce = QPushButton(self)
        self.pushButton_ce.setText('CE')
        self.pushButton_ce.setGeometry(QRect(320, 170, 51, 61))

        self.pushButton_p = QPushButton(self)
        self.pushButton_p.setText('+')
        self.pushButton_p.setGeometry(QRect(180, 110, 51, 61))

        self.pushButton_m = QPushButton(self)
        self.pushButton_m.setText('-')
        self.pushButton_m.setGeometry(QRect(180, 170, 51, 61))

        self.pushButton_mu = QPushButton(self)
        self.pushButton_mu.setText('*')
        self.pushButton_mu.setGeometry(QRect(180, 230, 51, 61))

        self.pushButton_di = QPushButton(self)
        self.pushButton_di.setText('/')
        self.pushButton_di.setGeometry(QRect(180, 290, 51, 61))

        self.pushButton_po = QPushButton(self)
        self.pushButton_po.setText('^')
        self.pushButton_po.setGeometry(QRect(240, 110, 51, 61))

        self.pushButton_pe = QPushButton(self)
        self.pushButton_pe.setText('%')
        self.pushButton_pe.setGeometry(QRect(240, 170, 51, 61))

        self.pushButton = QPushButton(self)
        self.pushButton.setText('=')
        self.pushButton.setGeometry(QRect(240, 230, 131, 122))
        self.pushButton_0.clicked.connect(lambda: self.butt_click(self.pushButton_0))
        self.pushButton_1.clicked.connect(lambda: self.butt_click(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.butt_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.butt_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.butt_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.butt_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.butt_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.butt_click(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.butt_click(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.butt_click(self.pushButton_9))
        self.pushButton_c.clicked.connect(lambda: self.butt_click(self.pushButton_c))
        self.pushButton_p.clicked.connect(lambda: self.butt_click(self.pushButton_p))
        self.pushButton_pe.clicked.connect(lambda: self.butt_click(self.pushButton_pe))
        self.pushButton_po.clicked.connect(lambda: self.butt_click(self.pushButton_po))
        self.pushButton_di.clicked.connect(lambda: self.butt_click(self.pushButton_di))
        self.pushButton_mu.clicked.connect(lambda: self.butt_click(self.pushButton_mu))
        self.pushButton_m.clicked.connect(lambda: self.butt_click(self.pushButton_m))
        self.pushButton_d.clicked.connect(lambda: self.butt_click(self.pushButton_d))
        self.pushButton_ce.clicked.connect(lambda: self.butt_click(self.pushButton_ce))
        self.pushButton.clicked.connect(lambda: self.butt_click(self.pushButton))
        self.show()

    def butt_click(self,b):

        global num
        global num1
        global num2

        if b.text() == "C":
            self.textEdit.clear()
        elif b.text() == "CE":
            self.textEdit.backspace()
        elif b.text() == "=":
            z = self.textEdit.toPlainText()
            if z[0] == "+":
                self.textEdit.setText(str(float(num1+num2)))
            elif z[0] == "-":
                self.textEdit.setText(str(float(num1-num2)))
            elif z[0] == "*":
                self.textEdit.setText(str(float((num1*num2))))
            elif z[0] == "/":
                self.textEdit.setText(str(float((num1/num2))))
            elif z[0] == "%":
                self.textEdit.setText(str(float(num1%num2)))
            elif z[0] == "^":
                self.textEdit.setText(str(float(num1**num2)))
            num=0
            c=self.textEdit.toPlainText()
            num1= float(c)
            num2=0

        elif b.text() == "+":
                c = b.text()
                num=1
                self.textEdit.clear()
                self.textEdit.setText(c)
                
        elif b.text() == "-":
                c = b.text()
                num=1
                self.textEdit.clear()
                self.textEdit.setText(c)
        elif b.text() == "*":
                c = b.text()
                num=1
                self.textEdit.clear()
                self.textEdit.setText(c)
        elif b.text() == "/":
                c = b.text()
                num1
                self.textEdit.clear()
                self.textEdit.setText(c)

        elif b.text() == "^":
                c = b.text()
                num=1
                self.textEdit.clear()
                self.textEdit.setText(c)

        elif b.text() == "%":
                c = b.text()
                num=1
                self.textEdit.clear()
                self.textEdit.setText(c)


        else:
            c = self.textEdit.toPlainText() + b.text()
            self.textEdit.setText(c)
            z = self.textEdit.toPlainText()
            if num ==1:
                num2= float(z[1:]) 
            else :
                num1= float(z[0:])
                
app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())










