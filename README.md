# PySide2 Examples <!-- omit in toc -->
PySide2 in VFX.

Blog:[VFXのためのPySideまとめ](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html) (Japanese only.)

## Contents: <!-- omit in toc -->

- [System Environment:](#system-environment)
- [Release Note:](#release-note)
- [Installation:](#installation)
- [Darkstyle:](#darkstyle)
- [Import PySide2:](#import-pyside2)
  - [Example1:](#example1)
  - [Example2:](#example2)
  - [Example3:](#example3)
- [Qt.py](#qtpy)
  - [Example:](#example)

## System Environment:
* Window10
* Python 3.7.9
* PySide2 (Qt 5.15.2)

## Release Note:
2024/02/13
Test

2022/09/13
- Added:
  - QComboBox

2022/08/01
- Added:
  - QSpacer


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

### Example:
```Python
try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from Qt import QtCore, QtGui, QtWidgets
```