import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtCore import Qt


class ExampleDotsWindow(QWidget):
    def __init__(self):
        super(ExampleDotsWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Dots draw example')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_points(painter)
        painter.end()

    def draw_points(self, painter):
        painter.setPen(Qt.red)
        size = self.size()

        points = ((random.randint(1, size.width() - 1), random.randint(1, size.height() - 1))
                  for _ in range(1000))
        for point in points:
            painter.drawPoint(point[0], point[1])


def main(args):
    app = QApplication(args)
    example = ExampleDotsWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
