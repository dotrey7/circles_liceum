import sys
from random import randint

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QFont, QPixmap, QTransform, QColor, QIcon, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QComboBox, QListWidgetItem, \
    QWidget, QLabel, QMessageBox, QDialog, QTextEdit, QTableWidget, QTableWidgetItem, QAbstractItemView, QPlainTextEdit
from PyQt6 import uic


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.do)
        self.exec = False

    def do(self):
        self.exec = True
        self.update()

    def paintEvent(self, event):
        if self.exec:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.exec = False

    def draw(self, qp):
        qp.setBrush(QColor('yellow'))
        radius = randint(0, 200)
        qp.drawEllipse(QPoint(300, 250), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
