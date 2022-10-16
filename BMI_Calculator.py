from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
 
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi("BMI Calculator.ui", self)
        self.Calculate_Button.clicked.connect(self.onClick)
        # Height_input = self.Height_Input.text()
        # Weight_input = self.Weight_Input.text()
        # Height_input.textChanged.connect(self.onEnter)
        # Weight_input.textChanged.connect(self.onEnter)

    def onEnter(self,Height_input, Weight_input):
        print(Height_input, Weight_input)

    def onClick(self):
        Height_input = self.Height_Input.text()
        Weight_input = self.Weight_Input.text()
        BMI_Result_Calculated = (Weight_input/(Height_input)**2)*703
        print(BMI_Result_Calculated)
        self.BMI_Result.incomeChanged.connect(BMI_result_calculated.display)


locals()
app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
