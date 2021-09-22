import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ExampleSliderWindow(QWidget):
    def __init__(self):
        super(ExampleSliderWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.change_value)

        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap(os.environ['img1']))
        self.label.setGeometry(160, 40, 80, 80)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider example')

    def change_value(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap(os.environ['img1']))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap(os.environ['img2']))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap(os.environ['img3']))
        else:
            self.label.setPixmap(QPixmap(os.environ['img4']))


def main(args):
    app = QApplication(args)
    example = ExampleSliderWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
