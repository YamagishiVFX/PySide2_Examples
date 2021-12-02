import sys

from PySide2 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(400, 150)
        self.setWindowTitle('MyMainWinodw')

        #--------------------------------------#
        # Setup CentralWidget
        #--------------------------------------#
        layout = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)

        # QPushButton
        self.button = QtWidgets.QPushButton('Push Button')
        layout.addWidget(self.button)

        self.setCentralWidget(self.widget)

        #--------------------------------------#
        # Setup Status Bar
        #--------------------------------------#
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        #--------------------------------------#
        # menuBar
        #--------------------------------------#
        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)
        
        self.menu_file = QtWidgets.QMenu('File', self)
        self.menubar.addAction(self.menu_file.menuAction())

        action = QtWidgets.QAction('Exit', self)
        self.menu_file.addAction(action)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    
    sys.exit(app.exec_())