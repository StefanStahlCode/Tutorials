import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc
import PySide6.QtGui as pg

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = pq.QLabel("context menu test")

        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = pq.QMenu(self)
        context.addAction(pg.QAction("test 1", self))
        context.addAction(pg.QAction("test 2", self))
        context.addAction(pg.QAction("test 3", self))
        context.exec_(e.globalPos())
        

if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()