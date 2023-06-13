import sys
import PySide6.QtWidgets as pq
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize
class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar App")

        label = pq.QLabel("This is a label")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = pq.QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        #for QAction the parent for the action is passed as the last item, here self
        #Adding an Icon by adding QIcon(filename) to the QAction
        button_action = QAction(QIcon("application-blue.png"), "Your Button", self)
        button_action.setStatusTip("This is a button")
        #making the button toogleable
        button_action.setCheckable(True)
        button_action.triggered.connect(self.tool_button_click)
        #.setToolButtonStyle can be used to change how the button is displayed, default is to follow the system settings
        #Qt.ToolButtonIconOnly	Icon only, no text
        #Qt.ToolButtonTextOnly	Text only, no icon
        #Qt.ToolButtonTextBesideIcon	Icon and text, with text beside the icon
        #Qt.ToolButtonTextUnderIcon	Icon and text, with text under the icon
        #Qt.ToolButtonFollowStyle	Follow the host desktop style
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bank.png"), "Button 2", self)
        button_action2.setStatusTip("Second button")
        button_action2.triggered.connect(self.tool_button_click)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(pq.QLabel("Hello"))
        toolbar.addWidget(pq.QCheckBox())



        #adding menubar
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

        #adding a keyboard shortcut 
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        
        #adding a Status Bar
        self.setStatusBar(pq.QStatusBar(self))

    def tool_button_click(self, s):
        print("click", s)




if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()