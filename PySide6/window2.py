import sys
import PySide6.QtWidgets as pq
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize
from random import randint


class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This")
        self.w = None
        self.second_window = AnotherWindow()
        self.third_window = AnotherWindow()
        layout = pq.QVBoxLayout()
        self.button = pq.QPushButton("Open Window")
        self.button.clicked.connect(self.show_new_window)
        self.second_button = pq.QPushButton("Show second window")
        self.second_button.clicked.connect(self.toggle_second_window)
        self.third_button = pq.QPushButton("Show the third button")
        self.third_button.clicked.connect(self.toggle_window_3)
        layout.addWidget(self.button)
        layout.addWidget(self.second_button)
        layout.addWidget(self.third_button)

        central_widget = pq.QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else: #clicking on the button again will close the window and the next button press will open the window again, as the none check is passed
            self.w.close()
            self.w = None

    def toggle_second_window(self, checked):
        if self.second_window.isVisible():
            self.second_window.hide()
        else:
            self.second_window.show()

    def toggle_window_3(self, checked):
        if self.third_window.isVisible():
            self.third_window.hide()
        else:
            self.third_window.show()

class AnotherWindow(pq.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = pq.QHBoxLayout()
        self.label = pq.QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

        
    
if __name__ == "__main__":
    app = pq.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    app.exec()