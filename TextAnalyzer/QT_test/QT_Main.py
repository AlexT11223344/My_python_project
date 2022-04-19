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
        self.Qslider_sense.valueChanged.connect(self.Qslider_operation)
        self.Qslider_sense.valueChanged.connect(self.fuzzyMatch_lineEditor_receiveData)
        self.lineEdit_FuzzyMatch.editingFinished.connect(self.fuzzyMatch_lineEditor_sendData)

        '''<---------------------------  UI  --------------------------->'''
        self.setWindowTitle("Text Analyzer")
        self.setWindowIcon(QIcon("icon.png"))
        # Table KWIC
        self.table_KWIC.setColumnCount(5)
        self.table_KWIC.setHorizontalHeaderLabels(["File Name", "RowCount", "Left Context", "Hit", "Right context"])
        self.table_KWIC.setColumnWidth(0, 300)
        self.table_KWIC.setColumnWidth(1, 100)
        self.table_KWIC.setColumnWidth(2, 350)
        self.table_KWIC.setColumnWidth(3, 100)
        self.table_KWIC.setColumnWidth(4, 350)

        # Qslider
        self.Qslider_sense.setMinimum(0)
        self.Qslider_sense.setMaximum(100)
        self.Qslider_sense.setSingleStep(1)
        self.Qslider_sense.setValue(70)
        _layout = self.makeContent(self.Qslider_sense)
        self.setLayout(_layout)

    '''
    *****************************************************************************************************************************************
    *****************************************************************************************************************************************
    *****************************************************************************************************************************************
    *****************************************************************************************************************************************
    *****************************************************************************************************************************************
    *****************************************************************************************************************************************
    '''

    '''<---------------------------  Menu Bar  --------------------------->'''

    # 1. open_file
    def open_file(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName()
        # pending : valid the txt documents
        if file_path:
            self.file_name = Path(file_path).name
            self.file_path_dic.update({self.file_name: file_path})
            self.listWidget.addItem(self.file_name)

    # 2. close
    def exit(self):
        self.file_path_dic.clear()
        self.close()


    def search_input_1(self):
        self.query_1 = self.input_1.text()
        # QtWidgets.QMessageBox.about(self, "Please load txt file first")
        if not self.query_1:
            QtWidgets.QMessageBox.about(self, "No key words", "Please enter your key word.")
        elif self.textBrowser_1.find(self.query_1):
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
        else:
            file_name_list, row_Count_list, leftContext, hit, rightContext = keyword_l_r(self.file_read, self.item_text,
                                                                                     self.query_2, 10, self.senseValue)

            # self.textBrowser_1.setText(''.join(rightContext[0:len(rightContext)]))
            self.table_KWIC.clearContents()
            self.table_KWIC.setRowCount(len(file_name_list))

            for i in range(0, len(file_name_list)):
                # add id to column_1
                # id_Item = QTableWidgetItem(id_list[i])
                # self.table_KWIC.setItem(i, 0, id_Item)

                # add file_name to column_1
                fileName_Item = QTableWidgetItem(file_name_list[i])
                self.table_KWIC.setItem(i, 0, fileName_Item)

                # add row_count to column_2
                rowCount_Item = QTableWidgetItem(row_Count_list[i])
                self.table_KWIC.setItem(i, 1, rowCount_Item)

                # add leftContext to column_3
                leftContext_Item = QTableWidgetItem(leftContext[i])
                self.table_KWIC.setItem(i, 2, leftContext_Item)

                # add hit to column_4
                hit_Item = QTableWidgetItem(hit[i])
                self.table_KWIC.setItem(i, 3, hit_Item)

                # add rightContext to column_5
                lrightContext_Item = QTableWidgetItem(rightContext[i])
                self.table_KWIC.setItem(i, 4, lrightContext_Item)

            _layout = self.makeContent(self.table_KWIC)
            self.setLayout(_layout)
            self.label_QueryResult_2.setText(str(len(row_Count_list)))

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

    def Qslider_operation(self):
        print('current slider value=%s' % self.Qslider_sense.value())
        self.senseValue = self.Qslider_sense.value()

    def fuzzyMatch_lineEditor_receiveData(self):
        self.lineEdit_FuzzyMatch.setText(str(self.senseValue))

    def fuzzyMatch_lineEditor_sendData(self):
        self.check = self.lineEdit_FuzzyMatch.text()
        self.check = int(self.check)
        if isinstance(self.check, int) == True and 0 <= self.check <= 100:
            self.senseValue = self.check
            self.Qslider_sense.setValue(self.check)
        else:
            pass


    def makeContent(self, template):
        layout = QVBoxLayout()
        layout.addWidget(template)
        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
