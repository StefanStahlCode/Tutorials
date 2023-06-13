import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.checkbox = pq.QCheckBox("This is a checkbox")
        self.checkbox.setCheckState(pc.Qt.CheckState.Checked)

        self.checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(self.checkbox)


    def show_state(self, state):
        print(state == pc.Qt.CheckState.Checked.value)
        print(pc.Qt.CheckState.Checked.value)
        print(state)

#for tristate use either widget.setCheckstate(pc.Qt.PartiallyChecked)
#or widget.setTriState(True)


#set checkbox state with either 
#.setChecked(True/False)
#or .setCheckState() which accepts Qt.CheckState.Unchecked , Qt.CheckState.PartiallyChecked , Qt.CheckState.Checked

#print(state) witll result in checked = 2 , unchecked = 0 , partially checked = 1
#-> Qt.CheckState.Checked = 2


if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()