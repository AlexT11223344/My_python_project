import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QTdesigner_MainWindow import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.display_list_wideget()
        self.search_1.clicked.connect(self.search_input_1)
        self.actionOpen_File.triggered.connect(self.open_file)

    def display_list_wideget(self):
        item = ['x']
        self.listWidget.addItems(item)

    def search_input_1(self):
        query = self.input_1.text()
        if not query:
            QtWidgets.QMessageBox.about(self, "No key words", "Please enter your key word.")
        print(query)

    def open_file(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName()
        if file_path:
            self.textBrowser_1.setText(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
