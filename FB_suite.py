import sys
#pyqt6 imports fr
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("fun-bucks portal")
        welcome = Qwidget("welcome to the fun-bucks portal")
        layout = QVBoxlayout()
        layout.addwidget(welcome)

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
