import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.label = pq.QLabel("Hello")
        self.label_2 = pq.QLabel("1")
        self.label_2.setText("2")
        #set font size
        font = self.label.font()
        font.setPointSize(30)
        #there are 4 Alignment flags for horizontal Alignment
        #Qt.AlignmentFlag.AlignLeft	Aligns with the left edge.
        #Qt.AlignmentFlag.AlignRight	Aligns with the right edge.
        #Qt.AlignmentFlag.AlignHCenter	Centers horizontally in the available space.
        #Qt.AlignmentFlag.AlignJustify	Justifies the text in the available space.
        #There are 3  Flags for vertical Alignmnent
        #Qt.AlignmentFlag.AlignTop	Aligns with the top.
        #Qt.AlignmentFlag.AlignBottom	Aligns with the bottom.
        #Qt.AlignmentFlag.AlignVCenter	Centers vertically in the available space.
        #You can combine flags together using pipes (|), however
        #you can only use the vertical or horizontal alignment flag at a time
        #Qt.AlignmentFlag.AlignCenter	Centers horizontally and vertically

        self.label.setFont(font)
        self.label.setAlignment(pc.Qt.AlignmentFlag.AlignHCenter | pc.Qt.AlignmentFlag.AlignVCenter)

        #.setPixmap() can be used display an Image on a label
        self.setCentralWidget(self.label)



if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()