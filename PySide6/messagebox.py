import sys
import PySide6.QtWidgets as pq


class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = pq.QPushButton("Open Dialog")
        #button.clicked.connect(self.button_clicked)
        #button.clicked.connect(self.button_message)
        #button.clicked.connect(self.built_in_message_box)
        button.clicked.connect(self.button_argument)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dia = pq.QMessageBox(self)
        dia.setWindowTitle("Question!!")
        dia.setText("Simple")

        button=dia.exec()

        if button == pq.QMessageBox.Ok:
            print("Ok")

        #QMessageBox has similar to Qdialogbox buttons to use and combine with |:
            #QMessageBox.Ok
            #QMessageBox.Open
            #QMessageBox.Save
            #QMessageBox.Cancel
            #QMessageBox.Close
            #QMessageBox.Discard
            #QMessageBox.Apply
            #QMessageBox.Reset
            #QMessageBox.RestoreDefaults
            #QMessageBox.Help
            #QMessageBox.SaveAll
            #QMessageBox.Yes
            #QMessageBox.YesToAll
            #QMessageBox.No
            #QMessageBox.NoToAll
            #QMessageBox.Abort
            #QMessageBox.Retry
            #QMessageBox.Ignore
            #QMessageBox.NoButton
        #tweaking the icon with:
            #QMessageBox.NoIcon	The message box does not have an icon.
            #QMessageBox.Question	The message is asking a question.
            #QMessageBox.Information	The message is informational only.
            #QMessageBox.Warning	The message is warning.
            #QMessageBox.Critical	The message indicates a critical problem

    def button_message(self, s):
        dia = pq.QMessageBox(self)
        dia.setWindowTitle("message")
        dia.setText("box")
        dia.setStandardButtons(pq.QMessageBox.Yes | pq.QMessageBox.No)
        dia.setIcon(pq.QMessageBox.Question)
        button = dia.exec()

        if button == pq.QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

    #using built in methods of a messagebox
    #QMessageBox.about(parent, title, message)
    #QMessageBox.critical(parent, title, message)
    #QMessageBox.information(parent, title, message)
    #QMessageBox.question(parent, title, message)
    #QMessageBox.warning(parent, title, message)
    #this version doesn't need to call the .exec() function
    def built_in_message_box(self, s):
        button = pq.QMessageBox.question(self, "Question Dialog", "The longer Message")

        if button == pq.QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

    #information, question, warning and critical accept button and defaultButton arguments
    def button_argument(self):
        button = pq.QMessageBox.critical(
            self, 
            "Oh dear", 
            "Very Very Wrong",
            buttons = pq.QMessageBox.Discard | pq.QMessageBox.NoToAll | pq.QMessageBox.Ignore,
            defaultButton=pq.QMessageBox.Discard            
        )

        if button == pq.QMessageBox.Discard:
            print("Discard!")
        elif button == pq.QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()