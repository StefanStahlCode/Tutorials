import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.spinbox = pq.QSpinBox()
        #self.dspinbox = pq.QDoubleSpinBox()

        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(3)
        #self.dspinbox.setRange(-10, 3)
        #both set minimum + set maximum and set range can be used for bot spinbox and double spinbox
        self.spinbox.setPrefix("$")
        self.spinbox.setSuffix("c")
        #suffixes and prefixes can be added to add currencies, units or other value types
        self.spinbox.setSingleStep(3) #0.5 for double spinbox
        self.spinbox.valueChanged.connect(self.value_changed)
        self.spinbox.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(self.spinbox)

    def value_changed(self, value):
        print(value)
    
    def value_changed_str(self, val_str):
        print(val_str)

    





if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()