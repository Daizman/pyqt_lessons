import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QMouseEvent, QDragEnterEvent, QDropEvent


class MyButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if e.buttons() != Qt.RightButton:
            return

        mime_data = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        drop_action = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        QPushButton.mousePressEvent(self, e)

        if e.button() == Qt.LeftButton:
            print('press')


class ExampleDragButtonWindow(QWidget):
    def __init__(self):
        super(ExampleDragButtonWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setAcceptDrops(True)

        self.button = MyButton('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Drag button example')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        a0.accept()

    def dropEvent(self, a0: QDropEvent) -> None:
        pos = a0.pos()
        self.button.move(pos)

        a0.setDropAction(Qt.MoveAction)
        a0.accept()


def main(args):
    app = QApplication(args)
    example = ExampleDragButtonWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
