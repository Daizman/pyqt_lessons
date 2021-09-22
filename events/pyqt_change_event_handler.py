import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt


class ExampleChangeEventHandlerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Change event handler example')

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.key() == Qt.Key_Escape:
            self.close()


def main(args):
    app = QApplication(args)
    example = ExampleChangeEventHandlerWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
