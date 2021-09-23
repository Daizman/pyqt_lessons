import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QPaintEvent
from PyQt5.QtCore import Qt


class ExamplePenWindow(QWidget):
    def __init__(self):
        super(ExamplePenWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Pen usage example')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_lines(painter)
        painter.end()

    def draw_lines(self, painter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 3, 6, 2])
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)


def main(args):
    app = QApplication(args)
    example = ExamplePenWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
