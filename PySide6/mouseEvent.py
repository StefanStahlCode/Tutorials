import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc
import PySide6.QtGui as pg

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = pq.QLabel("Click the window")

        self.setCentralWidget(self.label)
        
        

    #defining different mouse events
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
    #separating mouse buttons into left middle and right clicks
    def mousePressEvent(self, e):
        if e.button() == pc.Qt.LeftButton:
            self.label.setText("mousePressEvent Left")
        
        elif e.button() == pc.Qt.MiddleButton:
            self.label.setText("mosePressEvent Middle")
        
        elif e.button() == pc.Qt.RightButton:
            self.label.setText("mousePressEvent Right")

    def mouseReleaseEvent(self, e):
        if e.button() == pc.Qt.LeftButton:
            self.label.setText("mouseReleaseEvent Left")
        
        elif e.button() == pc.Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent Middle")
        
        elif e.button() == pc.Qt.RightButton:
            self.label.setText("mouseReleaseEvent Right")
    
    #you can can make a custom event while still retaining the original event behavior by using super and calling the original event
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent Left")
        super().mouseDoubleClickEvent(e)

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