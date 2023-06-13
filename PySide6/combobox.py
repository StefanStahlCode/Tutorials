import sys
import PySide6.QtWidgets as pq
import PySide6.QtCore as pc

class MainWindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.combox = pq.QComboBox()
        self.combox.addItems(["One", "Two", "Three"])

        self.combox.currentIndexChanged.connect(self.index_changed)

        self.combox.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.combox)

    def index_changed(self, index): 
        print(index)

    def text_changed(self, text): 
        print(text)

    #.currentChangedIndex gives the index of the selected item while .currentChangedText returns the label of the item as a String

    #combox can be made editable with combox.setEditable(True)

    # combox.setInsertPolicy can be used to set flags on how to add items
    #QComboBox.NoInsert	No insert
    #QComboBox.InsertAtTop	Insert as first item
    #QComboBox.InsertAtCurrent	Replace currently selected item
    #QComboBox.InsertAtBottom	Insert after last item
    #QComboBox.InsertAfterCurrent	Insert after current item
    #QComboBox.InsertBeforeCurrent	Insert before current item
    #QComboBox.InsertAlphabetically	Insert in alphabetical order

    #combox.setMaxCount(10) is used to set a maximum limit



if __name__ == "__main__":
    app = pq.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()