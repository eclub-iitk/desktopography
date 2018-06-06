import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QFrame)
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MouseTracker(QWidget):
    
    global x, y
    x=0
    y=0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        global x, y
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Mouse Tracker')
        #self.setRotation(60)
        self.label = QLabel(self)
        self.label.resize(200, 100)
        
        self.ellipse = QGraphicsEllipseItem(10, 20, 100, 60)
        self.ellipse.setTransformOriginPoint(QPointF(100/2+10, 60/2+20)) 
        self.ellipse.setRotation(-60)
        self.scene.addItem(self.ellipse)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(x, y, 100, 100)
        self.show()


    def mouseMoveEvent(self, event):
        global x, y
        x= event.x()
        y=event.y()
        self.frame.setGeometry(x, y, 100, 100)
        
        #self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())