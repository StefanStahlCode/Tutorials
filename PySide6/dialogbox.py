import sys
import PySide6.QtWidgets as pq


class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("My App")

        button = pq.QPushButton("Open Dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    
    def button_clicked(self, s):
        print(s)
        dia = CusstomDialog(self)
        if dia.exec():
            print("success")
        else:
            print("Canceled")
        

class CusstomDialog(pq.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialog Window")

        #Creating dialog Buttons, this way you don't need to worry about satisfiying host desktop standards
        #fist defining which buttons to use
            #QDialogButtonBox has the follwing Buttons for this:
            #QDialogButtonBox.Ok
            #QDialogButtonBox.Open
            #QDialogButtonBox.Save
            #QDialogButtonBox.Cancel
            #QDialogButtonBox.Close
            #QDialogButtonBox.Discard
            #QDialogButtonBox.Apply
            #QDialogButtonBox.Reset
            #QDialogButtonBox.RestoreDefaults
            #QDialogButtonBox.Help
            #QDialogButtonBox.SaveAll
            #QDialogButtonBox.Yes
            #QDialogButtonBox.YesToAll
            #QDialogButtonBox.No
            #QDialogButtonBox.Abort
            #QDialogButtonBox.Retry
            #QDialogButtonBox.Ignore
            #QDialogButtonBox.NoButton
        #Multiple can be used together by using a pipe | 
        #Qt will handle the Order according to platform standards
        button_box = pq.QDialogButtonBox.Ok | pq.QDialogButtonBox.Cancel


        self.buttonBox = pq.QDialogButtonBox(button_box)
        #connecting accepetd and rejected methods to buttons ok and cancel
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = pq.QVBoxLayout()
        message = pq.QLabel("Something happend, ok?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)










if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()