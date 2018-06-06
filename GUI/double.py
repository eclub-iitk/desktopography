import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer
import time
class exam(QWidget):

	def __init__(self):
		super().__init__()
		self.fun()

	global num
	num=0
	global num1, num2
	num1=0
	num2=0

	def fun(self):
		self.setWindowTitle("experiment")
		self.setGeometry(400,400,400,400)
		but = QPushButton(self)
		but.resize(400,400)
		but.setStyleSheet("background-color: red")
		but.clicked.connect(lambda: self.click(but))
		
		self.show()
	def click(self, but):
		global num, num1, num2
		but.setStyleSheet("background-color: white")
		but.setText("")
		num1=time.time()
		self.detect(but)
		


	def detect(self, but):
		
		global num, num1, num2
		
		time = num1 - num2
		print("time")
		print(time)
		#if num is 0:
		#	num2  = num1
		#	num = 1
		#	print("return")
		#	return

		#else :
		if time < 0.5:
			print("Double click")
			num =0
			self.double(but)
			return
		num2 = num1
		num = 1

	def double(self, but):
		but.setText("Jay")
		but.setStyleSheet("background-color: red")
		



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = exam()
	sys.exit(app.exec_())


