import sys

from PySide2 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    
    sys.exit(app.exec_())