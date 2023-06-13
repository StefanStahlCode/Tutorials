import sys
import PySide6.QtWidgets as pq
import PySide6.QtGui as pg


class colorPalette(pq.QWidget):

    def __init__(self, color):
        super(colorPalette, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(pg.QPalette.Window, pg.QColor(color))
        self.setPalette(palette)

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = pq.QVBoxLayout()
        button_layout = pq.QHBoxLayout()
        self.stacklayout = pq.QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = pq.QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(colorPalette("red"))

        btn = pq.QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(colorPalette("green"))

        btn = pq.QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(colorPalette("yellow"))

        widget = pq.QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()