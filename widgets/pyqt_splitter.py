import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory
from PyQt5.QtCore import Qt


class ExampleSplitterWindow(QWidget):
    def __init__(self):
        super(ExampleSplitterWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout(self)

        top_left = QFrame(self)
        top_left.setFrameShape(QFrame.StyledPanel)

        top_right = QFrame(self)
        top_right.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        h_box.addWidget(splitter2)
        self.setLayout(h_box)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Splitter example')


def main(args):
    app = QApplication(args)
    example = ExampleSplitterWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
