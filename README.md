# PySide2 Examples
My Blog:[VFXのためのPySideまとめ](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html) (Japanese only.)

## Environment:
* Window10
* Python 3.7.9
* PySide2 (Qt 5.15.2)

## Installation:
**PySide2:** https://pypi.org/project/PySide2/
```
python -m pip install --upgrade pip
pip install PySide2
```

**check PySide2**
```
pip show PySide2
```
### Darkstyle
**QDarkstyle:** https://pypi.org/project/QDarkStyle/
```
pip install QDarkStyle
```

## Import PySide2:
### Example1:
```Python
import sys

from PySide2 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QWidget()
    view.show()
    sys.exit(app.exec_())
```
### Example2:
```Python
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
```
### Example3:
```Python
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
```
## Examples 
* QDialog
