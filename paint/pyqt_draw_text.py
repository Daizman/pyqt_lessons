import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPaintEvent
from PyQt5.QtCore import Qt


class ExampleDrawTextWindow(QWidget):
    def __init__(self):
        super(ExampleDrawTextWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.text = 'Тестовый текст для приложения'

        self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('Draw text example')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)  # все рисование должно происходить между begin и end
        self.draw_text(a0, painter)
        painter.end()

    def draw_text(self, event, painter):
        painter.setPen(QColor(168, 68, 168))
        painter.setFont(QFont('Decorative', 10))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)


def main(args):
    app = QApplication(args)
    example = ExampleDrawTextWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)

