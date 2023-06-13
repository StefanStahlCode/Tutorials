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

        tabs = pq.QTabWidget()
        tabs.setTabPosition(pq.QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "blue", "green", "yellow"]):
            tabs.addTab(colorPalette(color), color)

        self.setCentralWidget(tabs)




if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()