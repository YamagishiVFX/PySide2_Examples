import sys

from PySide2 import QtWidgets, QtCore

""" Get Window Size
Reference from :
* https://stackoverflow.com/questions/43126721/detect-resizing-in-widget-window-resized-signal

"""

class MyWidget(QtWidgets.QWidget):
    resized = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resized.connect(self.size_changed)


    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    
    def size_changed(self):
        print(f'{self.width()} {self.height()}')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    view = MyWidget()
    view.show()

    app.exec_()