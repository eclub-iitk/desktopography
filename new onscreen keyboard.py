# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    global c 
    c=0       
    global d
    d=0
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 560)
        Dialog.setWhatsThis("")
        Dialog.setStyleSheet("background-color:rgb(12, 46, 95);")
        self.pushButton_55 = QtWidgets.QPushButton(Dialog)
        self.pushButton_55.setGeometry(QtCore.QRect(-150, 370, 51, 61))
        self.pushButton_55.setObjectName("pushButton_55")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 1051, 91))
        self.frame_2.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButton_2.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 70, 70))
        self.pushButton_3.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton_4.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}\n"
"\n"
"QPushButton:pressed {border:5px}\n"
"\n"
"QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}\n"
"\n"
"font: 20pt \"DejaVu Sans\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(490, 10, 70, 70))
        self.pushButton_9.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 10, 70, 70))
        self.pushButton_10.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 10, 70, 70))
        self.pushButton_6.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 10, 70, 70))
        self.pushButton_7.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(730, 10, 70, 70))
        self.pushButton_11.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);\n"
"font: 20pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed {border:5px}\n"
"QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(810, 10, 70, 70))
        self.pushButton_12.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 10, 70, 70))
        self.pushButton_5.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(889, 10, 151, 70))
        self.pushButton_15.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color:rgb(247, 9, 9);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_67.setGeometry(QtCore.QRect(570, 10, 70, 70))
        self.pushButton_67.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_67.setObjectName("pushButton_67")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(20, 190, 1051, 91))
        self.frame_3.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_32.setGeometry(QtCore.QRect(970, 10, 70, 70))
        self.pushButton_32.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_25.setGeometry(QtCore.QRect(570, 10, 70, 70))
        self.pushButton_25.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_22.setGeometry(QtCore.QRect(330, 10, 70, 70))
        self.pushButton_22.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_23.setGeometry(QtCore.QRect(410, 10, 70, 70))
        self.pushButton_23.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_27.setGeometry(QtCore.QRect(730, 10, 70, 70))
        self.pushButton_27.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_26.setGeometry(QtCore.QRect(650, 10, 70, 70))
        self.pushButton_26.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_31.setGeometry(QtCore.QRect(890, 10, 70, 70))
        self.pushButton_31.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_30.setGeometry(QtCore.QRect(810, 10, 70, 70))
        self.pushButton_30.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_19.setGeometry(QtCore.QRect(90, 10, 70, 70))
        self.pushButton_19.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_20.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton_20.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButton_18.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_21.setGeometry(QtCore.QRect(250, 10, 70, 70))
        self.pushButton_21.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_24.setGeometry(QtCore.QRect(490, 10, 70, 70))
        self.pushButton_24.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 280, 1051, 91))
        self.frame_4.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_93 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_93.setGeometry(QtCore.QRect(490, 10, 70, 70))
        self.pushButton_93.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_88 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_88.setGeometry(QtCore.QRect(90, 10, 70, 70))
        self.pushButton_88.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_90.setGeometry(QtCore.QRect(250, 10, 70, 70))
        self.pushButton_90.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_89 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_89.setGeometry(QtCore.QRect(730, 10, 70, 70))
        self.pushButton_89.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_95.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButton_95.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_91 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_91.setGeometry(QtCore.QRect(330, 10, 70, 70))
        self.pushButton_91.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_102 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_102.setGeometry(QtCore.QRect(570, 10, 70, 70))
        self.pushButton_102.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_94.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton_94.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_96.setGeometry(QtCore.QRect(810, 10, 70, 70))
        self.pushButton_96.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_100 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_100.setGeometry(QtCore.QRect(410, 10, 70, 70))
        self.pushButton_100.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_92.setGeometry(QtCore.QRect(650, 10, 70, 70))
        self.pushButton_92.setStyleSheet("QPushButton{\n"
"    font: 20pt;\n"
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
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_99 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_99.setGeometry(QtCore.QRect(890, 10, 151, 70))
        self.pushButton_99.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(63, 230, 132);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_99.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../237272-Keyboard_enter_1-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_99.setIcon(icon)
        self.pushButton_99.setIconSize(QtCore.QSize(100, 50))
        self.pushButton_99.setObjectName("pushButton_99")
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(20, 370, 1051, 91))
        self.frame_5.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_106 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_106.setGeometry(QtCore.QRect(10, 10, 151, 70))
        self.pushButton_106.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(31, 190, 207);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_116 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_116.setGeometry(QtCore.QRect(410, 10, 70, 70))
        self.pushButton_116.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_116.setObjectName("pushButton_116")
        self.pushButton_108 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_108.setGeometry(QtCore.QRect(490, 10, 70, 70))
        self.pushButton_108.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_108.setObjectName("pushButton_108")
        self.pushButton_115 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_115.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton_115.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_115.setObjectName("pushButton_115")
        self.pushButton_104 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_104.setGeometry(QtCore.QRect(650, 10, 70, 70))
        self.pushButton_104.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_112 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_112.setGeometry(QtCore.QRect(570, 10, 70, 70))
        self.pushButton_112.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_109 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_109.setGeometry(QtCore.QRect(330, 10, 70, 70))
        self.pushButton_109.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_107 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_107.setGeometry(QtCore.QRect(250, 10, 70, 70))
        self.pushButton_107.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_111 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_111.setGeometry(QtCore.QRect(730, 10, 70, 70))
        self.pushButton_111.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_114 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_114.setGeometry(QtCore.QRect(810, 10, 70, 70))
        self.pushButton_114.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_113 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_113.setGeometry(QtCore.QRect(890, 10, 151, 70))
        self.pushButton_113.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(31, 190, 207);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_113.setObjectName("pushButton_113")
        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(20, 460, 1051, 91))
        self.frame_6.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 10, 391, 70))
        self.pushButton_8.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(255, 255, 255);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_119 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_119.setGeometry(QtCore.QRect(9, 10, 151, 70))
        self.pushButton_119.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(24, 94, 102);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_119.setObjectName("pushButton_119")
        self.pushButton_105 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_105.setGeometry(QtCore.QRect(730, 10, 70, 70))
        self.pushButton_105.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_120 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_120.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton_120.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_120.setObjectName("pushButton_120")
        self.pushButton_121 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_121.setGeometry(QtCore.QRect(890, 10, 151, 70))
        self.pushButton_121.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color:rgb(237, 212, 0);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_121.setObjectName("pushButton_121")
        self.pushButton_122 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_122.setGeometry(QtCore.QRect(250, 10, 70, 70))
        self.pushButton_122.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_122.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../117556_email_512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_122.setIcon(icon1)
        self.pushButton_122.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_122.setObjectName("pushButton_122")
        self.frame_7 = QtWidgets.QFrame(Dialog)
        self.frame_7.setGeometry(QtCore.QRect(20, 10, 1051, 91))
        self.frame_7.setStyleSheet("font: 20pt \"DejaVu Sans\";")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 10, 151, 70))
        self.pushButton_28.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color:  rgb(245, 121, 0);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setGeometry(QtCore.QRect(170, 10, 70, 70))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(46, 52, 54);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(245, 121, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_13.setGeometry(QtCore.QRect(880, 10, 70, 70))
        self.pushButton_13.setStyleSheet("QPushButton{border:none;border-radius:8px;background-color: rgb(46, 52, 54);color:rgb(255, 255, 255);}QPushButton:pressed {border:5px}QPushButton:hover{background-color: rgb(245, 121, 0);color:rgb(255, 255, 255);}")
        self.pushButton_13.setObjectName("pushButton_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "virtual keyboard"))
        self.pushButton_55.setText(_translate("Dialog", "4"))
        self.pushButton_2.setText(_translate("Dialog", "1  !"))
        self.pushButton_3.setText(_translate("Dialog", "2  @"))
        self.pushButton_4.setText(_translate("Dialog", "3  #"))
        self.pushButton_9.setText(_translate("Dialog", "7 &&"))
        self.pushButton_10.setText(_translate("Dialog", "9  ("))
        self.pushButton_6.setText(_translate("Dialog", "5  %"))
        self.pushButton_7.setText(_translate("Dialog", "6  ^"))
        self.pushButton_11.setText(_translate("Dialog", "0  )"))
        self.pushButton_12.setText(_translate("Dialog", "-  _"))
        self.pushButton_5.setText(_translate("Dialog", "4  $"))
        self.pushButton_15.setText(_translate("Dialog", "Back"))
        self.pushButton_67.setText(_translate("Dialog", "8  *"))
        self.pushButton_32.setText(_translate("Dialog", "}   ]"))
        self.pushButton_25.setText(_translate("Dialog", "i"))
        self.pushButton_22.setText(_translate("Dialog", "t"))
        self.pushButton_23.setText(_translate("Dialog", "y"))
        self.pushButton_27.setText(_translate("Dialog", "p"))
        self.pushButton_26.setText(_translate("Dialog", "o"))
        self.pushButton_31.setText(_translate("Dialog", "{   [  "))
        self.pushButton_30.setText(_translate("Dialog", "\\  |"))
        self.pushButton_19.setText(_translate("Dialog", "w"))
        self.pushButton_20.setText(_translate("Dialog", "e"))
        self.pushButton_18.setText(_translate("Dialog", "q"))
        self.pushButton_21.setText(_translate("Dialog", "r"))
        self.pushButton_24.setText(_translate("Dialog", "u"))
        self.pushButton_93.setText(_translate("Dialog", "h"))
        self.pushButton_88.setText(_translate("Dialog", "a"))
        self.pushButton_90.setText(_translate("Dialog", "d"))
        self.pushButton_89.setText(_translate("Dialog", ";   :"))
        self.pushButton_95.setText(_translate("Dialog", "caps"))
        self.pushButton_91.setText(_translate("Dialog", "f"))
        self.pushButton_102.setText(_translate("Dialog", "j"))
        self.pushButton_94.setText(_translate("Dialog", "s"))
        self.pushButton_96.setText(_translate("Dialog", "\'   \""))
        self.pushButton_100.setText(_translate("Dialog", "g"))
        self.pushButton_92.setText(_translate("Dialog", "k"))
        self.pushButton_106.setText(_translate("Dialog", "shift"))
        self.pushButton_116.setText(_translate("Dialog", "v"))
        self.pushButton_108.setText(_translate("Dialog", "b"))
        self.pushButton_115.setText(_translate("Dialog", "z"))
        self.pushButton_104.setText(_translate("Dialog", "m"))
        self.pushButton_112.setText(_translate("Dialog", "n"))
        self.pushButton_109.setText(_translate("Dialog", "c"))
        self.pushButton_107.setText(_translate("Dialog", "x"))
        self.pushButton_111.setText(_translate("Dialog", ",  <"))
        self.pushButton_114.setText(_translate("Dialog", ".  >"))
        self.pushButton_113.setText(_translate("Dialog", "shift"))
        self.pushButton_8.setText(_translate("Dialog", "&"))
        self.pushButton_119.setText(_translate("Dialog", "ctrl"))
        self.pushButton_105.setText(_translate("Dialog", "/  ?"))
        self.pushButton_120.setText(_translate("Dialog", "alt"))
        self.pushButton_121.setText(_translate("Dialog", "ctrl"))
        self.pushButton_28.setText(_translate("Dialog", "tab"))
        self.pushButton.setText(_translate("Dialog", "`  ~"))
        self.pushButton_13.setText(_translate("Dialog", "=  +"))

        self.pushButton_55.clicked.connect(lambda: self.butt_click(self.pushButton_55))
        self.pushButton_2.clicked.connect(lambda: self.butt_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.butt_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.butt_click(self.pushButton_4))
        self.pushButton_9.clicked.connect(lambda: self.butt_click(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.butt_click(self.pushButton_10))
        self.pushButton_6.clicked.connect(lambda: self.butt_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.butt_click(self.pushButton_7))
        self.pushButton_11.clicked.connect(lambda: self.butt_click(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.butt_click(self.pushButton_12))
        self.pushButton_5.clicked.connect(lambda: self.butt_click(self.pushButton_5))
        self.pushButton_15.clicked.connect(lambda: self.butt_click(self.pushButton_15))
        self.pushButton_67.clicked.connect(lambda: self.butt_click(self.pushButton_67))
        self.pushButton_32.clicked.connect(lambda: self.butt_click(self.pushButton_32))
        self.pushButton_25.clicked.connect(lambda: self.butt_click(self.pushButton_25))
        self.pushButton_22.clicked.connect(lambda: self.butt_click(self.pushButton_22))
        self.pushButton_23.clicked.connect(lambda: self.butt_click(self.pushButton_23))
        self.pushButton_27.clicked.connect(lambda: self.butt_click(self.pushButton_27))
        self.pushButton_26.clicked.connect(lambda: self.butt_click(self.pushButton_26))
        self.pushButton_31.clicked.connect(lambda: self.butt_click(self.pushButton_31))
        self.pushButton_30.clicked.connect(lambda: self.butt_click(self.pushButton_30))
        self.pushButton_19.clicked.connect(lambda: self.butt_click(self.pushButton_19))
        self.pushButton_20.clicked.connect(lambda: self.butt_click(self.pushButton_20))
        self.pushButton_18.clicked.connect(lambda: self.butt_click(self.pushButton_18))
        self.pushButton_21.clicked.connect(lambda: self.butt_click(self.pushButton_21))
        self.pushButton_24.clicked.connect(lambda: self.butt_click(self.pushButton_24))
        self.pushButton_93.clicked.connect(lambda: self.butt_click(self.pushButton_93))
        self.pushButton_88.clicked.connect(lambda: self.butt_click(self.pushButton_88))
        self.pushButton_90.clicked.connect(lambda: self.butt_click(self.pushButton_90))
        self.pushButton_89.clicked.connect(lambda: self.butt_click(self.pushButton_89))
        self.pushButton_95.clicked.connect(lambda: self.butt_click(self.pushButton_95))
        self.pushButton_91.clicked.connect(lambda: self.butt_click(self.pushButton_91))
        self.pushButton_102.clicked.connect(lambda: self.butt_click(self.pushButton_102))
        self.pushButton_94.clicked.connect(lambda: self.butt_click(self.pushButton_94))
        self.pushButton_96.clicked.connect(lambda: self.butt_click(self.pushButton_96))
        self.pushButton_100.clicked.connect(lambda: self.butt_click(self.pushButton_100))
        self.pushButton_92.clicked.connect(lambda: self.butt_click(self.pushButton_92))
        self.pushButton_106.clicked.connect(lambda: self.butt_click(self.pushButton_106))
        self.pushButton_116.clicked.connect(lambda: self.butt_click(self.pushButton_116))
        self.pushButton_108.clicked.connect(lambda: self.butt_click(self.pushButton_108))
        self.pushButton_115.clicked.connect(lambda: self.butt_click(self.pushButton_115))
        self.pushButton_104.clicked.connect(lambda: self.butt_click(self.pushButton_104))
        self.pushButton_112.clicked.connect(lambda: self.butt_click(self.pushButton_112))
        self.pushButton_109.clicked.connect(lambda: self.butt_click(self.pushButton_109))
        self.pushButton_107.clicked.connect(lambda: self.butt_click(self.pushButton_107))
        self.pushButton_111.clicked.connect(lambda: self.butt_click(self.pushButton_111))
        self.pushButton_114.clicked.connect(lambda: self.butt_click(self.pushButton_114))
        self.pushButton_113.clicked.connect(lambda: self.butt_click(self.pushButton_113))
        self.pushButton_8.clicked.connect(lambda: self.butt_click(self.pushButton_8))
        self.pushButton_119.clicked.connect(lambda: self.butt_click(self.pushButton_119))
        self.pushButton_105.clicked.connect(lambda: self.butt_click(self.pushButton_105))
        self.pushButton_120.clicked.connect(lambda: self.butt_click(self.pushButton_120))
        self.pushButton_121.clicked.connect(lambda: self.butt_click(self.pushButton_121))
        self.pushButton_28.clicked.connect(lambda: self.butt_click(self.pushButton_28))
        self.pushButton.clicked.connect(lambda: self.butt_click(self.pushButton))
        self.pushButton_13.clicked.connect(lambda: self.butt_click(self.pushButton_13))


    def butt_click(self,b):
        global c
        global d
        global e
        z=b.text()
        if b.text()=='shift':
            if c==1 :
                c=0
            else :
                c = 1
        elif b.text()=='caps':
            if d==1 :
                d=0
            else : 
                d=1 
        elif b.text()=='tab':
            print ('   ', end = '')
        
        elif b.text()=='enter':
            print ()
        elif b.text()=='space':
            print(end='')
       
        else :                
		#print (b.text()) 
            if c==1 :
                if (z[0]=='1' or z[0]=='2' or  z[0]=='3' or  z[0]=='4' or  z[0]=='5' or  z[0]=='6' or  z[0]=='7' or  z[0]=='8' or  z[0]=='9' or  z[0]=='`' or  z[0]=='-' or z[0]=='=' or z[0]==',' or z[0]=='.' or z[0]=='//' or z[0]=='[' or z[0]==']' or z[0]=='\\' ) :
		    #print (z[2], end="")
                    #c = 0
                    print(z[3], end='')
                    c = 0
                else :
                    var = b.text()
                    ascii = ord(var) 
                    newvar = ascii -32 
                    print (chr(newvar),end = '')  
                    c=0    
            
            elif d==1 :
                var = z[0] 
                ascii = ord(var) 
                newvar = ascii -32 
                print (chr(newvar),end = '')
		    	
	    
            else:
                #print("1")
                print (z[0],end = '')    
				   
			


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

