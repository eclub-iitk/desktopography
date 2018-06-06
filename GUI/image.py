import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    global x,y
    x=0
    y=0
    def __init__(self):
       QWidget.__init__(self)
       self.setMouseTracking(True)

       self.height = 1000
       self.width = 1000
       self.setGeometry(100,100,self.height,self.width)
       self.setStyleSheet("background-color: white")

       #color = widget.palette().color(QPalette.Background)
       #print (color.red(), color.green(), color.blue())

       global x,y

       button = QPushButton(self)
       button.move(0,0)
       button.resize(500,500)
       #button.setText("WEll this is a button")
       button.setStyleSheet("background-color: white; border:none")
       #button.setAutoFillBackground(TRUE) 
       button.clicked.connect(lambda: self.click(button))
       button.setToolTip('heyyyy')
       icon = QIcon("test.jpg")
       #icon.move(0,0)
       button.setIcon(icon)
       #button.setContentsMargins(10, 10, 10, 10)
       button.setIconSize(QSize(500,500))

        #self.label  = QLabel(self)
      # self.label.setOpenExternalLinks(True)
       #self.label.setPixmap(QPixmap('test.jpg'))
       #self.label.setGeometry(100,100,100,100)
       self.show()


    def click(self, but):
        #but.setStyleSheet("background-color: white")
        #self.setGeometry(100,100,1500,1500)
        #but.setText("YO bro")
        print('hey bro')

    def mouseMoveEvent(self, event):
        global x, y
        x= event.x()
        y=event.y()
        #print(x,y)
        if x in range(510) and y in range(510):
            print('yes')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())