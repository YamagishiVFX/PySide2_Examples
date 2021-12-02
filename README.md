# PySide2_Examples
## Environment:
* Window10
* Python 3.7.9
* PySide2 (Qt 5.15.2)

## Import PySide2:
```Python
import sys

from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import (
    Qt
)
from PySide2.QtGui import (
    QColor
)
from PySide2.QtWidgets import (
    QApplication,
    QWidget
)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  view = QtWidgets.QWidget()
  view.show()
  sys.exit(app.exec_())
```

## QDialog
