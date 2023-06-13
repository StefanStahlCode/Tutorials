import sys
import PySide6.QtWidgets as pq
from PySide6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PySide6.QtCore import Qt, QSize

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        layout = pq.QGridLayout()
        
        la1 = pq.QLabel("Hello")
        la1.setFrameShape(pq.QFrame.Panel)
        la2 = pq.QLabel("this")
        la2.setFrameShape(pq.QFrame.Panel)
        la3 = pq.QLabel("loooooong")
        la3.setFrameShape(pq.QFrame.Panel)
        layout.addWidget(la1, 0, 0)
        layout.addWidget(la2, 0, 1)
        layout.addWidget(la3, 1, 0, 1, 2)

        widget = pq.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        

def main():
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()