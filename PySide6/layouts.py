import sys
import PySide6.QtWidgets as pq
import PySide6.QtGui as pg

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setAutoFillBackground(True)

        #4 types of layouts:
        #QHBoxLayout	Linear horizontal layout
        #QVBoxLayout	Linear vertical layout
        #QGridLayout	In indexable grid XxY
        #QStackedLayout	Stacked (z) in front of one another
        #while horintal and vertical layouts can be nested, 
        #here only the gridlayout is used
        #QstackedLayout can be used to create a tab like interface
        layout = pq.QGridLayout()
        #first number horizontal position, second number vertical position
        layout.addWidget(colorPalette("red"), 0, 0)
        layout.addWidget(colorPalette("green"), 1, 0)
        layout.addWidget(colorPalette("blue"), 1, 1)
        layout.addWidget(colorPalette("purple"), 2, 1)

        widget = pq.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




#creating a widget to display a color
class colorPalette(pq.QWidget):

    def __init__(self, color):
        super(colorPalette, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(pg.QPalette.Window, pg.QColor(color))
        self.setPalette(palette)






if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()