import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame
from PyQt5.QtGui import QColor


class ExampleToggleButtonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.color = QColor(0, 0, 0)

        red_b = QPushButton('Red', self)
        red_b.move(10, 10)
        red_b.setCheckable(True)
        red_b.clicked[bool].connect(self.change_color)

        green_b = QPushButton('Green', self)
        green_b.move(10, 60)
        green_b.setCheckable(True)
        green_b.clicked[bool].connect(self.change_color)

        blue_b = QPushButton('Blue', self)
        blue_b.move(10, 110)
        blue_b.setCheckable(True)
        blue_b.clicked[bool].connect(self.change_color)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s }' % self.color.name())

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button example')

    def change_color(self, pressed):
        source = self.sender()

        value = 255 if pressed else 0

        if source.text() == 'Red':
            self.color.setRed(value)
        elif source.text() == 'Green':
            self.color.setGreen(value)
        else:
            self.color.setBlue(value)

        self.square.setStyleSheet('QWidget { background-color: %s }' % self.color.name())


def main(args):
    app = QApplication(args)
    example = ExampleToggleButtonWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
