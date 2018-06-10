import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()

        self.button = QtWidgets.QPushButton('karan')
        self.button.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button1 = QtWidgets.QPushButton('alok')
        self.button1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button2 = QtWidgets.QPushButton('vaish')
        self.button2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button3 = QtWidgets.QPushButton('vaish1')
        self.button3.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button4 = QtWidgets.QPushButton('vaish2')
        self.button4.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button5 = QtWidgets.QPushButton('vaish3')
        self.button5.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button6 = QtWidgets.QPushButton('vaish4')
        self.button6.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button7 = QtWidgets.QPushButton('vaish5')
        self.button7.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button8 = QtWidgets.QPushButton('vaish6')
        self.button8.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.button)
        v_layout.addWidget(self.button1)
        v_layout.addWidget(self.button2)
        v1_layout = QVBoxLayout()
        v1_layout.addWidget(self.button3)
        v1_layout.addWidget(self.button4)
        v1_layout.addWidget(self.button5)
        v2_layout = QVBoxLayout()
        v2_layout.addWidget(self.button6)
        v2_layout.addWidget(self.button7)
        v2_layout.addWidget(self.button8)


        grid.addLayout(v_layout ,0 ,0 ,1, 1)
        grid.addLayout(v1_layout, 0 ,1 ,1, 1)
        grid.addLayout(v2_layout, 0 ,2 ,1 ,1)



        self.setLayout(grid)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Notepad()
    sys.exit(app.exec_())


