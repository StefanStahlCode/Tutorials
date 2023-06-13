import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.slider = pq.QSlider()
        #self.slider = pq.QSlider(pc.Qt.Orientation.Vertical)
        #self.slider = pq.QSlider(pc.Qt.Orientation.Horizontal)
        #for specififying orientation 
        
        self.slider.setMinimum(-12)
        self.slider.setMaximum(6)
        #alternatively .setRange(-12, 6)

        self.slider.setSingleStep(3)

        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(self.slider)


    def value_changed(self, value):
        print(value)

    def slider_position(self, position):
        print("position", position)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")




if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()