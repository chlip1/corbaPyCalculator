import sys
from omniORB import CORBA
import Calculator
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("calculator.ui", self)
		self.initCorba()
		self.expression = ''
		self.sign = ''
		self.val1, self.val2 = 0, 0
		self.button_1.clicked.connect(lambda: self.addToExpression(1))
		self.button_2.clicked.connect(lambda: self.addToExpression(2))
		self.button_3.clicked.connect(lambda: self.addToExpression(3))
		self.button_4.clicked.connect(lambda: self.addToExpression(4))
		self.button_5.clicked.connect(lambda: self.addToExpression(5))
		self.button_6.clicked.connect(lambda: self.addToExpression(6))
		self.button_7.clicked.connect(lambda: self.addToExpression(7))
		self.button_8.clicked.connect(lambda: self.addToExpression(8))
		self.button_9.clicked.connect(lambda: self.addToExpression(9))
		self.button_0.clicked.connect(lambda: self.addToExpression(0))
		self.button_point.clicked.connect(lambda: self.addToExpression("."))
		self.button_sum.clicked.connect(lambda: self.signClicked("+"))
		self.button_subtract.clicked.connect(lambda: self.signClicked("-"))
		self.button_multiply.clicked.connect(lambda: self.signClicked("*"))
		self.button_divide.clicked.connect(lambda: self.signClicked("/"))
		self.button_clear.clicked.connect(self.clear)
		self.button_equal.clicked.connect(self.equal)

	def initCorba(self):
		orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
		ior = sys.argv[1]
		obj = orb.string_to_object(ior)
		self.eo = obj._narrow(Calculator.Calc)
		if self.eo is None:
			print("Object reference is not an Example::Echo")
			sys.exit(1)

	def addToExpression(self, val):
		self.expression = self.expression + str(val)
		self.result_label.setText(self.expression)

	def signClicked(self, sign):
		if self.expression != '':
			self.sign = sign
			self.val1 = float(self.expression)
			self.expression = ''
			self.result_label.setText(self.expression)
	
	def clear(self):
		self.expression = self.expression[:-1]
		self.result_label.setText(self.expression)

	def equal(self):
		if self.val1 != 0:
			self.val2 = float(self.expression)
			self.expression=''
			if self.sign == "+": result = self.eo.sum(self.val1, self.val2)
			elif self.sign == "-": result = self.eo.subtract(self.val1, self.val2)
			elif self.sign == "*": result = self.eo.multiply(self.val1, self.val2)
			elif self.sign == "/": result = self.eo.divide(self.val1, self.val2)
			self.result_label.setText(str(result))

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
