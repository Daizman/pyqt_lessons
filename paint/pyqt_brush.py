import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush
from PyQt5.QtCore import Qt


class ExampleBrushWindow(QWidget):
    def __init__(self):
        super(ExampleBrushWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Brush usage example')

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        ExampleBrushWindow.draw_textures(painter)
        painter.end()

    @staticmethod
    def draw_textures(painter):
        brush = QBrush()
        patterns = [Qt.SolidPattern,
                    Qt.Dense1Pattern,
                    Qt.Dense2Pattern,
                    Qt.DiagCrossPattern,
                    Qt.Dense4Pattern,
                    Qt.Dense6Pattern,
                    Qt.HorPattern,
                    Qt.VerPattern,
                    Qt.BDiagPattern]

        x = [10, 130, 250]
        y = [15, 105, 195]
        W = 90
        H = 60

        for i, l in enumerate(x):
            for j, t in enumerate(y):
                brush.setStyle(patterns[i * 3 + j])
                painter.setBrush(brush)
                painter.drawRect(l, t, W, H)


def main(args):
    app = QApplication(args)
    example = ExampleBrushWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
