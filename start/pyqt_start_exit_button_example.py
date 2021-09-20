import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class ExampleButtonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        button = QPushButton('Exit', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(button.sizeHint())  # .sizeHint() - подгон необходимого размера
        button.move(50, 50)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Quit button example')


def main(args):
    app = QApplication(args)
    example = ExampleButtonWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
