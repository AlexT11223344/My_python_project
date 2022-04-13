import sys
import filetype
import os

from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHBoxLayout, QVBoxLayout, \
    QTableView
from QTdesigner_MainWindow import *
from model_keyword import *
from pathlib import Path
from PyQt5.QtGui import QTextCharFormat, QPalette, QTextCursor, QTextDocument, QColor, QIcon, QStandardItemModel, \
    QStandardItem


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        '''<---------------------------  Parameter  --------------------------->'''
        self.file_path_dic = {}

        '''<---------------------------  Action  --------------------------->'''
        self.search_1.clicked.connect(self.search_input_1)
        self.search_2.clicked.connect(self.search_input_2)
        self.actionOpen_File.triggered.connect(self.open_file)
        self.actionExit.triggered.connect(self.exit)
        self.listWidget.itemDoubleClicked.connect(self.list_widget_double_click)

        '''<---------------------------  UI  --------------------------->'''
        self.setWindowTitle("Text Analyzer")
        self.setWindowIcon(QIcon("icon.png"))
        # set KWIC UI
        self.table_KWIC.setColumnCount(4)
        self.table_KWIC.setHorizontalHeaderLabels(["File Name", "Left Context", "Hit", "Right context"])
        # self.table_KWIC.setColumnWidth(0, 50)
        self.table_KWIC.setColumnWidth(0, 200)
        self.table_KWIC.setColumnWidth(1, 350)
        self.table_KWIC.setColumnWidth(2, 100)
        self.table_KWIC.setColumnWidth(3, 350)

    def search_input_1(self):
        self.query_1 = self.input_1.text()
        # QtWidgets.QMessageBox.about(self, "Please load txt file first")
        if not self.query_1:
            QtWidgets.QMessageBox.about(self, "No key words", "Please enter your key word.")
        if self.textBrowser_1.find(self.query_1):
            palette = self.textBrowser_1.palette()
            # palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
            palette.setColor(QPalette.Highlight, QColor(64, 224, 205))
            self.textBrowser_1.setPalette(palette)
            # self.textBrowser_1.find(self.query)
        else:
            QtWidgets.QMessageBox.about(self, "No content for this query")

    def search_input_2(self):
        self.query_2 = self.input_2.text()
        if not self.query_2:
            QtWidgets.QMessageBox.about(self, "No key words", "Please enter your key word.")
        file_name_list, leftContext, hit, rightContext = keyword_l_r(self.file_read, self.item_text,
                                                                              self.query_2, 8)
        # self.textBrowser_1.setText(''.join(id_list[0:len(id_list)]))
        self.table_KWIC.clearContents()
        self.table_KWIC.setRowCount(len(file_name_list))

        for i in range(0, len(file_name_list)):
            # add id to column_1
            # id_Item = QTableWidgetItem(id_list[i])
            # self.table_KWIC.setItem(i, 0, id_Item)

            # add file_name to column_2
            fileName_Item = QTableWidgetItem(file_name_list[i])
            self.table_KWIC.setItem(i, 0, fileName_Item)

            # add leftContext to column_3
            leftContext_Item = QTableWidgetItem(leftContext[i])
            self.table_KWIC.setItem(i, 1, leftContext_Item)

            # add hit to column_4
            hit_Item = QTableWidgetItem(hit[i])
            self.table_KWIC.setItem(i, 2, hit_Item)

            # add rightContext to column_5
            lrightContext_Item = QTableWidgetItem(rightContext[i])
            self.table_KWIC.setItem(i, 3, lrightContext_Item)
        layout = self.makeContent(self.table_KWIC)
        self.setLayout(layout)

    def open_file(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName()
        # pending : valid the txt documents
        if file_path:
            self.file_name = Path(file_path).name
            self.file_path_dic.update({self.file_name: file_path})
            self.listWidget.addItem(self.file_name)

    def list_widget_double_click(self, item):
        # self.textBrowser_1.setText(self.file_path_dic[item.text()])
        self.item_text = item.text()
        file_path = self.file_path_dic[self.item_text]
        self.file_read = ""
        with open(file_path, 'r') as file:
            self.file_read = file.read()
            # for i in range(len(self.file_read)):
            #     self.textBrowser_1.setText(i)
            self.textBrowser_1.setText(self.file_read)

    def makeContent(self, template):
        layout = QVBoxLayout()
        layout.addWidget(template)
        return layout

    def exit(self):
        self.file_path_dic.clear()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
