import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.listwidget = pq.QListWidget()
        self.listwidget.addItems(["one", "two" , "three"])

        self.listwidget.currentItemChanged.connect(self.index_changed)
        self.listwidget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.listwidget)

    def index_changed(self, index): # Not an index, index is a QListWidgetItem
        print(index.text())
        print(index)

    def text_changed(self, text):
        print(text)

if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()