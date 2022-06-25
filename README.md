# PySide2 Examples
PySide2 in VFX.

Blog:[VFXのためのPySideまとめ](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html) (Japanese only.)

## Environment:
* Window10
* Python 3.7.9
* PySide2 (Qt 5.15.2)

## Relase Note:
2022/06/23
- Added : Quick Started

2022/06/11
- Updated : QTreeWidget

2022/06/10
- Added: QTreeWidget

## Installation:
**PySide2:** https://pypi.org/project/PySide2/
```
python -m pip install --upgrade pip
pip install PySide2
```

**Check PySide2**
```
pip list -o
pip show PySide2
```

**Updrade Package**
```
pip install -U PySide2
```
## Darkstyle:
**QDarkstyle:** https://pypi.org/project/QDarkStyle/
```
pip install QDarkStyle
```

## Import PySide2:
### Example1:
```Python
from PySide2 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QWidget()
    view.show()
    app.exec_()
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

## Qt.py
https://github.com/mottosso/Qt.py

### Import Example:
```Python
try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from Qt import QtCore, QtGui, QtWidgets
```

## Examples 
* QDialog
* QMainWindow
