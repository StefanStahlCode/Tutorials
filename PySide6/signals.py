import sys
import PySide6.QtWidgets as pq
import random

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWIndow(pq.QMainWindow):
    def __init__(self):
        #super allows direct access to methods from parent class without using name of base class
        super().__init__()  

        self.times_clicked = 0

        self.setWindowTitle("signals")

        

        #referencing a button with selfallows access in slots
        self.button = pq.QPushButton("Signal Test")
        #set button to toggable
        #self.button.setCheckable(True)
        #self.button.clicked.connect(self.button_released)
        #self.button.setChecked(self.button_checked)

        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.title_changed)


        self.setCentralWidget(self.button)


    def button_released(self):
        self.button_checked = self.button.isChecked()
        print(self.button_checked)
    
    def button_clicked(self):
        new_window_title = random.choice(window_titles)
        print("setting new title: %s" % new_window_title)
        #change window title
        self.setWindowTitle(new_window_title)

    def title_changed(self, title):
        print("the Title change to %s" % title)

        if title == "Something went wrong":
            self.button.setDisabled(True)

if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWIndow()
    window.show()

    app.exec_()
