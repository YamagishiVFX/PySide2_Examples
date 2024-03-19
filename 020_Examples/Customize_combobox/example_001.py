"""
Reference from
    * https://stackoverflow.com/questions/33124326/creating-a-custom-item-for-qcombobox-in-pyside

Info:
    * Coding by Tatsuya Yamagishi
    * Coding Python3.10 & PySide2
"""

import sys
from PySide2 import QtCore, QtGui, QtWidgets


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        self.item_model = QtGui.QStandardItemModel()
        self.setModel(self.item_model)

        self.activated.connect(self.activate_item)

    
    def activate_item(self, index):
        print(index)

        item = self.item_model.item(index)
        print(item)


    def add_items(self, items):
        for value in items:
            item = QtGui.QStandardItem(value)

            self.item_model.appendRow(item)


if __name__ == '__main__':
    items = ['1', '2', '3']


    app = QtWidgets.QApplication(sys.argv)
    view = ComboBox()
    view.add_items(items)

    view.show()
    app.exec_()