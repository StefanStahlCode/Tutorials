import sys
import PySide6.QtWidgets as pq
#collection of some qtwidgets more in the documentation 
class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        layout= pq.QVBoxLayout()
        widgets = [
            pq.QCheckBox,
            pq.QComboBox,
            pq.QDateEdit,
            pq.QDateTimeEdit,
            pq.QDial,
            pq.QDoubleSpinBox,
            pq.QFontComboBox,
            pq.QLCDNumber,
            pq.QLabel,
            pq.QLineEdit,
            pq.QProgressBar,
            pq.QPushButton,
            pq.QRadioButton,
            pq.QSlider,
            pq.QSpinBox,
            pq.QTimeEdit,
        ]

        for widget in widgets:
            layout.addWidget(widget())

        central_widget = pq.QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()