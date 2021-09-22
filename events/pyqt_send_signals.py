import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QMouseEvent


class Communicate(QObject):
    close_app = pyqtSignal()


class ExampleSendSignalsWindow(QMainWindow):
    def __init__(self):
        super(ExampleSendSignalsWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.communicate = Communicate()
        self.communicate.close_app.connect(self.close)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Send signal example')

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.communicate.close_app.emit()


def main(args):
    app = QApplication(args)
    example = ExampleSendSignalsWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
