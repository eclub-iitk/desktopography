from PyQt5 import QtCore, QtGui, QtWidgets
global width, height
global a,b
a=1080
b=720
width=751
height=561

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(a, b)
        Form.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 150, 301, 561))
        self.frame.setStyleSheet("QFrame{background-color: rgb(245, 121, 0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: transparent;\n"
"font: 75 25pt \"AnjaliOldLipi\";\n"
"color:rgb(46, 52, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border:5px\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(46, 52, 54);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 281, 100))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 281, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 281, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 340, 281, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 450, 281, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 20, 1071, 121))
        self.label.setStyleSheet("color:rgb(63, 230, 132);\n"
"font: 75 45pt \"AnjaliOldLipi\";\n"
"text-align: center;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(320, 150, width, height))
        self.frame_2.setStyleSheet("\n"
"QFrame{background-color: rgb(238, 238, 236);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QDial{\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color: transparent;\n"
"\n"
"color:rgb(46, 52, 54);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dial = QtWidgets.QDial(self.frame_2)
        self.dial.setGeometry(QtCore.QRect(10, 190, 201, 201))
        self.dial.setObjectName("dial")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(30, 90, 161, 41))
        self.progressBar.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.dial_2 = QtWidgets.QDial(self.frame_2)
        self.dial_2.setGeometry(QtCore.QRect(270, 190, 201, 201))
        self.dial_2.setObjectName("dial_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_2.setGeometry(QtCore.QRect(290, 90, 161, 41))
        self.progressBar_2.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.dial_3 = QtWidgets.QDial(self.frame_2)
        self.dial_3.setGeometry(QtCore.QRect(510, 190, 201, 201))
        self.dial_3.setObjectName("dial_3")
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_3.setGeometry(QtCore.QRect(530, 90, 161, 41))
        self.progressBar_3.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(70, 410, 111, 61))
        self.label_4.setStyleSheet("color:rgb(46, 52, 54);\n"
"font: 75 30pt \"AnjaliOldLipi\";\n"
"text-align: center;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(320, 410, 111, 61))
        self.label_5.setStyleSheet("color:rgb(46, 52, 54);\n"
"font: 75 30pt \"AnjaliOldLipi\";\n"
"text-align: center;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(570, 410, 111, 61))
        self.label_6.setStyleSheet("color:rgb(46, 52, 54);\n"
"font: 75 30pt \"AnjaliOldLipi\";\n"
"text-align: center;\n"
"")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.dial.valueChanged['int'].connect(self.progressBar.setValue)
        self.dial_2.valueChanged['int'].connect(self.progressBar_2.setValue)
        self.dial_3.valueChanged['int'].connect(self.progressBar_3.setValue)
        self.pushButton.clicked.connect(self.frame_2.show)

        def reset():
                global a,b
                a=1080
                b=720
                width=751
                height=561
                Form.resize(1080,720)
                self.frame_2.setGeometry(QtCore.QRect(320, 150, width, height))

        self.pushButton_3.clicked.connect(reset)

        def translate():
            global width, height, w_prev, h_prev, x1, x2,y1, y2,w1,w2
                
            width= Form.frameGeometry().width()
            height = Form.frameGeometry().height()
            x1=self.frame_2.frameGeometry().width()
            y1=self.frame_2.frameGeometry().height()
            x2=width*(320.0/1080.0)
            y2=height*(150.0/720.0)
            w1=width*(751/1080.0)
            w2=height*(561.0/720.0)
            print (width, x2)
            self.frame_2.setGeometry(QtCore.QRect(x2, y2, w1, w2 ))




        def btnclk2():
             translate() 

                
               
        self.pushButton_4.clicked.connect(btnclk2)
                    
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Fan"))
        self.pushButton_2.setText(_translate("Form", "Lights"))
        self.pushButton_3.setText(_translate("Form", "Cooler"))
        self.pushButton_4.setText(_translate("Form", "Music"))
        self.pushButton_5.setText(_translate("Form", "Lock"))
        self.label.setText(_translate("Form", "Electronics Club IoT Controller"))
        self.label_4.setText(_translate("Form", "Fan 1"))
        self.label_5.setText(_translate("Form", "Fan 2"))
        self.label_6.setText(_translate("Form", "Fan 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

