# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeWIndow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    global num

    num = 0

    def open(self):
        MainWindow1.close()
        Form1.show()

    def quit(self):
        MainWindow1.close()

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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
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
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton{\n"
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
        self.pushButton_1.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_d = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_d.setGeometry(QtCore.QRect(60, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_d.setFont(font)
        self.pushButton_d.setStyleSheet("QPushButton{\n"
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
        self.pushButton_d.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_d.setObjectName("pushButton_d")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton{\n"
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
        self.pushButton_0.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 260, 51, 61))
        self.pushButton_quit.setGeometry(QtCore.QRect(71, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_ce = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ce.setGeometry(QtCore.QRect(110, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ce.setFont(font)
        self.pushButton_ce.setStyleSheet("QPushButton{\n"
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
        self.pushButton_ce.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
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
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
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
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
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
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
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
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_di = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_di.setGeometry(QtCore.QRect(180, 320, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_di.setFont(font)
        self.pushButton_di.setStyleSheet("QPushButton{\n"
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
        self.pushButton_di.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_di.setObjectName("pushButton_di")
        self.pushButton_mu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mu.setGeometry(QtCore.QRect(180, 260, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_mu.setFont(font)
        self.pushButton_mu.setStyleSheet("QPushButton{\n"
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
        self.pushButton_mu.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_mu.setObjectName("pushButton_mu")
        self.pushButton_p = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_p.setGeometry(QtCore.QRect(180, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_p.setFont(font)
        self.pushButton_p.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_p.setStyleSheet("QPushButton{\n"
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
        self.pushButton_p.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_p.setObjectName("pushButton_p")
        self.pushButton_m = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_m.setGeometry(QtCore.QRect(180, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setStyleSheet("QPushButton{\n"
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
        self.pushButton_m.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_m.setObjectName("pushButton_m")
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c.setGeometry(QtCore.QRect(240, 140, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("QPushButton{\n"
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
        self.pushButton_c.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_po = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_p1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_p1.setGeometry(QtCore.QRect(10, 100, 51, 41))
        self.pushButton_po.setGeometry(QtCore.QRect(240, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_po.setFont(font)
        self.pushButton_po.setStyleSheet("QPushButton{\n"
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
        self.pushButton_po.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_po.setObjectName("pushButton_po")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 260, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 281, 75))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 200, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
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
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_d.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_quit.setText(_translate("MainWindow", "home"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_ce.setText(_translate("MainWindow", "CE"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_p1.setText(_translate("MainWindow", "back"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_di.setText(_translate("MainWindow", "/"))
        self.pushButton_mu.setText(_translate("MainWindow", "*"))
        self.pushButton_p.setText(_translate("MainWindow", "+"))
        self.pushButton_p.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_m.setText(_translate("MainWindow", "-"))
        self.pushButton_c.setText(_translate("MainWindow", "C"))
        self.pushButton_po.setText(_translate("MainWindow", "^"))
        self.pushButton.setText(_translate("MainWindow", "="))
        self.pushButton_6.setText(_translate("MainWindow", "6"))

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
        # self.pushButton_pe.clicked.connect(lambda: self.butt_click(self.pushButton_pe))
        self.pushButton_po.clicked.connect(lambda: self.butt_click(self.pushButton_po))
        self.pushButton_di.clicked.connect(lambda: self.butt_click(self.pushButton_di))
        self.pushButton_mu.clicked.connect(lambda: self.butt_click(self.pushButton_mu))
        self.pushButton_m.clicked.connect(lambda: self.butt_click(self.pushButton_m))
        self.pushButton_d.clicked.connect(lambda: self.butt_click(self.pushButton_d))
        self.pushButton_ce.clicked.connect(lambda: self.butt_click(self.pushButton_ce))
        self.pushButton.clicked.connect(lambda: self.butt_click(self.pushButton))
        self.pushButton_p1.clicked.connect(self.open)
        self.pushButton_quit.clicked.connect(self.quit)

    def butt_click(self, b):

        global num
        global num1
        global num2

        if b.text() == "C":
            self.textEdit.clear()
        elif b.text() == "CE":
            f = self.textEdit.toPlainText()
            x = len(f) - 1
            g = f[:x]
            self.textEdit.setText(g)

        elif b.text() == "=":
            z = self.textEdit.toPlainText()
            if z[0] == "+":
                self.textEdit.setText(str(float(num1 + num2)))
            elif z[0] == "-":
                self.textEdit.setText(str(float(num1 - num2)))
            elif z[0] == "*":
                self.textEdit.setText(str(float((num1 * num2))))
            elif z[0] == "/":
                self.textEdit.setText(str(float((num1 / num2))))
            elif z[0] == "%":
                self.textEdit.setText(str(float(num1 % num2)))
            elif z[0] == "^":
                self.textEdit.setText(str(float(num1 ** num2)))
            num = 0
            c = self.textEdit.toPlainText()
            num1 = float(c)
            num2 = 0

        elif b.text() == "+":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "-":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)
        elif b.text() == "*":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)
        elif b.text() == "/":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "^":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == "%":
            c = b.text()
            num = 1
            self.textEdit.clear()
            self.textEdit.setText(c)

        elif b.text() == ".":
            d = self.textEdit.toPlainText()
            if num == 0:
                if float(d[0:]) == int(d[0:]):
                    d = self.textEdit.toPlainText() + b.text()
                    self.textEdit.setText(d)

                else:
                    self, textEdit.setText(d)
            else:
                if float(d[1:]) == int(d[1:]):
                    d = self.textEdit.toPlainText() + b.text()
                    self.textEdit.setText(d)

                else:
                    self, textEdit.setText(d)


        else:
            c = self.textEdit.toPlainText() + b.text()
            self.textEdit.setText(c)
            z = self.textEdit.toPlainText()
            if num == 1:
                num2 = float(z[1:])
            else:
                num1 = float(z[0:])


class Ui_Form(object):
    def open(self):
        MainWindow1.show()
        Form1.close()

    def open1(self):
        Form1.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 556)
        Form.setStyleSheet(
            "border-image: url(:/newPrefix/3823a764f1e548212a77d243852e8dc0--shorts-movie-mobile-game.jpg);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 99, 91))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/video_game_icon-01.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 180, 99, 91))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/download.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 270, 99, 81))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/orange-next-512.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 370, 99, 101))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/racecar1.png);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.open1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "A BIT RACEY"))
        self.pushButton_2.setText(_translate("Form", "HOME"))
        self.pushButton_3.setText(_translate("Form", "CALCULATOR"))
        self.pushButton_4.setText(_translate("Form", "CONVERTER"))


class Ui_MainWindow(object):

    def open(self):
        Form1.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 646)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 170, 99, 81))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/3823a764f1e548212a77d243852e8dc0--shorts-movie-mobile-game.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "MENU"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Form1 = QtWidgets.QWidget()
    ui1 = Ui_Form()
    ui1.setupUi(Form1)
    MainWindow1 = QtWidgets.QMainWindow()
    ui2 = Ui_MainWindow1()
    ui2.setupUi(MainWindow1)
    MainWindow.show()
    sys.exit(app.exec_())
