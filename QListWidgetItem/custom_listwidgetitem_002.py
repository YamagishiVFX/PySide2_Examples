"""
Reference From:
https://stackoverflow.com/questions/25187444/pyqt-qlistwidget-custom-items
"""


from PySide2 import QtCore, QtGui, QtWidgets

ITEMS = [
    ('No.1', 'Meyoko', ),
    ('No.2', 'Nyaruko',),
    ('No.3', 'Louise', ),
]

class MyWidget(QtWidgets.QWidget):
    def __init__(self, item, parent = None):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.label_1 = QtWidgets.QLabel('Label_1')
        self.main_layout.addWidget(self.label_1)

        self.label_2 = QtWidgets.QLabel('Label_2')
        self.main_layout.addWidget(self.label_2)

        self.button = QtWidgets.QPushButton()
        self.main_layout.addWidget(self.button)

        self.setItem(item)

    def setItem(self, item):
        self.item = item

        self.label_1.text(item[0])
        self.label_2.text(item[1])

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.list = QtWidgets.QListWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.list)

    def addListItem(self, items):
        self.list.clear()
        for item in items:
            widget = MyWidget(item)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    for label in 'red blue green yellow purple'.split():
        window.addListItem(ITEMS)
    window.setGeometry(500, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())