import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPaintEvent


class ExampleColorsWindow(QWidget):
    def __init__(self):
        super(ExampleColorsWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 170)
        self.setWindowTitle('Draw colors example')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        ExampleColorsWindow.draw_colors(painter)
        painter.end()

    @staticmethod
    def draw_colors(painter):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        painter.setPen(color)

        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(10, 15, 90, 60)

        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(130, 15, 90, 60)

        painter.setBrush(QColor(25, 0, 90, 200))
        painter.drawRect(250, 15, 90, 60)


def main(args):
    app = QApplication(args)
    example = ExampleColorsWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
