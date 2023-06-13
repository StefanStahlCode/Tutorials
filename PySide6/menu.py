import sys
import PySide6.QtWidgets as pq
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__innit__()



if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()