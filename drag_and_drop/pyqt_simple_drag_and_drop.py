import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class MyButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        if a0.mimeData().hasFormat('text/plain'):
            a0.accept()
        else:
            a0.ignore()

    def dropEvent(self, a0: QDropEvent) -> None:
        self.setText(a0.mimeData().text())


class ExampleDragAndDropWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = MyButton('Btn', self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop example')
        self.setGeometry(300, 300, 250, 180)


def main(args):
    app = QApplication(args)
    example = ExampleDragAndDropWindow()  # выделить текст и перенести на кнопку
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
