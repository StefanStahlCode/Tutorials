import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        dial = pq.QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)

        #Note: signals are the same as for slider
        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.dial_position)
        dial.sliderPressed.connect(self.dial_pressed)
        dial.sliderReleased.connect(self.dial_released) 

        self.setCentralWidget(dial)

    def value_changed(self, value):
        print(value)

    def dial_position(self, position):
        print("position", position)

    def dial_pressed(self):
        print("Pressed!")

    def dial_released(self):
        print("Released")





if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()