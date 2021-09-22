import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class ExamplePixmapWindow(QWidget):
    def __init__(self):
        super(ExamplePixmapWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout(self)
        pixmap = QPixmap(os.environ['img1'])

        label = QLabel(self)
        label.setPixmap(pixmap)

        h_box.addWidget(label)
        self.setLayout(h_box)

        self.move(300, 200)
        self.setWindowTitle('Pixmap example')


def main(args):
    app = QApplication(args)
    example = ExamplePixmapWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
