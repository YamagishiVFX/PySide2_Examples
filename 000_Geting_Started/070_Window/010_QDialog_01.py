import sys

from PySide2.QtWidgets import (
    QApplication,
    QDialog
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ダイアログオブジェクト作成
dialog = QDialog()

# ウィンドウタイトルを変更
dialog.setWindowTitle('My Dialog')

# ウィンドウサイズの変更
dialog.resize(300, 200)

# ウィジェットの表示
dialog.show()

# アプリケーションメインループ開始
app.exec_()