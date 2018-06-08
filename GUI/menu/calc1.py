# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 380)
        MainWindow.setMinimumSize(QtCore.QSize(300, 380))
        MainWindow.setMaximumSize(QtCore.QSize(300, 380))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:  #2e3436;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_15.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(60, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_16.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_17.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_17.setObjectName("pushButton_17")
        self.but_dot = QtWidgets.QPushButton(self.centralwidget)
        self.but_dot.setGeometry(QtCore.QRect(60, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.but_dot.setFont(font)
        self.but_dot.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.but_dot.setIconSize(QtCore.QSize(50, 50))
        self.but_dot.setObjectName("but_dot")
        self.but_0 = QtWidgets.QPushButton(self.centralwidget)
        self.but_0.setGeometry(QtCore.QRect(10, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.but_0.setFont(font)
        self.but_0.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.but_0.setIconSize(QtCore.QSize(50, 50))
        self.but_0.setObjectName("but_0")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(60, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_22.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_22.setObjectName("pushButton_22")
        self.but_ce = QtWidgets.QPushButton(self.centralwidget)
        self.but_ce.setGeometry(QtCore.QRect(110, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.but_ce.setFont(font)
        self.but_ce.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.but_ce.setIconSize(QtCore.QSize(50, 50))
        self.but_ce.setObjectName("but_ce")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(110, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_24.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_25.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(60, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_26.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(110, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_27.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(180, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_28.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(180, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_29.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(180, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_30.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_30.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(180, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_31.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(240, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:   #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_32.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(240, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_33.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(240, 260, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:  #35372f;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_34.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_34.setObjectName("pushButton_34")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 281, 91))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"border:rgb(31, 190, 207);\n"
"border-size:3px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(110, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("QPushButton{\n"
"    font: 20pt \"Serif\";\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_35.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_35.setObjectName("pushButton_35")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_15.setText(_translate("MainWindow", "4"))
        self.pushButton_16.setText(_translate("MainWindow", "5"))
        self.pushButton_17.setText(_translate("MainWindow", "1"))
        self.but_dot.setText(_translate("MainWindow", "."))
        self.but_0.setText(_translate("MainWindow", "0"))
        self.pushButton_22.setText(_translate("MainWindow", "2"))
        self.but_ce.setText(_translate("MainWindow", "CE"))
        self.pushButton_24.setText(_translate("MainWindow", "3"))
        self.pushButton_25.setText(_translate("MainWindow", "7"))
        self.pushButton_26.setText(_translate("MainWindow", "8"))
        self.pushButton_27.setText(_translate("MainWindow", "9"))
        self.pushButton_28.setText(_translate("MainWindow", "/"))
        self.pushButton_29.setText(_translate("MainWindow", "*"))
        self.pushButton_30.setText(_translate("MainWindow", "+"))
        self.pushButton_30.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_31.setText(_translate("MainWindow", "-"))
        self.pushButton_32.setText(_translate("MainWindow", "C"))
        self.pushButton_33.setText(_translate("MainWindow", "^"))
        self.pushButton_34.setText(_translate("MainWindow", "="))
        self.pushButton_35.setText(_translate("MainWindow", "6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

