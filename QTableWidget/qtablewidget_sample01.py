import sys

from PySide2 import QtCore, QtGui, QtWidgets

LABELS = ['Name', 'ID', 'Description']
ITEMS = [
    ['Yamagishi', 10, 'CG Supervisor'],
    ['Arai', 11, 'VFX Artist'],
    ['Tanaka', 12, 'Compositor'],
]

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(450, 200)
        self.setWindowTitle('QTableWidget Sample')

        self.table = QtWidgets.QTableWidget(len(LABELS), len(ITEMS))
        self.table.setHorizontalHeaderLabels(LABELS)

        for i in range(len(LABELS)):
            for j in range(len(ITEMS)):
                item = QtWidgets.QTableWidgetItem(str(ITEMS[i][j]))
                self.table.setItem(i, j, item)

        self.table.setSortingEnabled(True)
        self.table.sortByColumn(0, QtCore.Qt.AscendingOrder)

        sizes = [150, 50, 200]
        header = self.table.horizontalHeader()
        # header.resizeSection(0, 100)
        for i in range(self.table.columnCount()):
            header.resizeSection(i, sizes[i])
            
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec_())