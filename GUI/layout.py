import sys
from PyQt5 import QtWidgets, QtGui ,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTextEdit
from PyQt5.QtCore import (Qt, QRect)
import resource_rc


class Window1(QWidget):
    def __init__(self, parent=None):
        super(Window1, self).__init__(parent)
        self.resize(831, 556)
        self.setStyleSheet("border-image: url(:/newPrefix/3823a764f1e548212a77d243852e8dc0--shorts-movie-mobile-game.jpg);")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 99, 91))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/video_game_icon-01.png);")
        self.pushButton.setText('A BIT RACEY')
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 180, 99, 91))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/download.png);")
        self.pushButton_2.setText('HOME')
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 270, 99, 81))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/orange-next-512.png);")
        self.pushButton_3.setText('CALCULATOR')
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 370, 99, 101))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/racecar1.png);")
        self.pushButton_4.setText('DESKTOP')
        self.show()


class Window(QWidget):
    global num3
    num3 = 0

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(400,380)

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
        self.pushButton_0.setText('7')
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
        self.pushButton_z = QPushButton(self)
        self.pushButton_z.setText('back')
        self.pushButton_z.setGeometry(QRect(0, 0 ,50 ,50))
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
        self.pushButton.clicked.connect(lambda: self.butt_click(self.pushButton))
        self.show()

    def butt_click(self, b):

        global num3
        global num1
        global num2

        if b.text() == "C":
            self.textEdit.clear()
        elif b.text() == "CE":
            self.textEdit.backspace()
        elif b.text() == "=":
            z = self.textEdit.toPlainText()
            if z[0] == "+":
                self.textEdit.setText(str(int(num1 + num2)))
            elif z[0] == "-":
                self.textEdit.setText(str(int(num1 - num2)))
            elif z[0] == "*":
                self.textEdit.setText(str(float((num1 * num2))))
            elif z[0] == "/":
                self.textEdit.setText(str(float((num1 / num2))))
            elif z[0] == "%":
                self.textEdit.setText(str(int(num1 % num2)))
            elif z[0] == "^":
                self.textEdit.setText(str(int(num1 ** num2)))
            num3 = 0

        elif b.text() == "+":
            c = b.text()
            num3 = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "-":
            c = b.text()
            num3 = 1
            self.textEdit.clear()
            self.textEdit.setText(c)
        elif b.text() == "*":
            c = b.text()
            num3 = 1
            self.textEdit.clear()
            self.textEdit.setText(c)
        elif b.text() == "/":
            c = b.text()
            num1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "^":
            c = b.text()
            num3 = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "%":
            c = b.text()
            num3 = 1
            self.textEdit.clear()
            self.textEdit.setText(c)


        else:
            c = self.textEdit.toPlainText() + b.text()
            self.textEdit.setText(c)
            z = self.textEdit.toPlainText()
            if num3 == 1:
                num2 = int(z[1:])
            else:
                num1 = int(z[0:])


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 831, 556)
        self.setStyleSheet("border-image: url(:/newPrefix/3823a764f1e548212a77d243852e8dc0--shorts-movie-mobile-game.jpg);")
        self.startUIToolTab()

    def startUIToolTab(self):
        self.ToolTab = Window1()
        self.setWindowTitle("UIToolTab")
        self.setCentralWidget(self.ToolTab)
        self.resize(831,556)
        self.setStyleSheet("border-image: url(:/newPrefix/3823a764f1e548212a77d243852e8dc0--shorts-movie-mobile-game.jpg);")
        self.ToolTab.pushButton_3.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.Window = Window()
        self.setWindowTitle("UIWindow")
        self.setCentralWidget(self.Window)
        self.resize(400,380)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Window.pushButton_z.clicked.connect(self.startUIToolTab)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


