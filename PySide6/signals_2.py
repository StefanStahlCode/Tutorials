import sys
import PySide6.QtWidgets as pq

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("signals_2")

        self.label = pq.QLabel()

        self.inputline = pq.QLineEdit()
        self.inputline.textChanged.connect(self.label.setText)

        layout = pq.QVBoxLayout()
        layout.addWidget(self.inputline)
        layout.addWidget(self.label)

        container = pq.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()